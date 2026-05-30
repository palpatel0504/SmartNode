import os
import shutil

from fastapi import FastAPI, UploadFile, File, HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, SessionLocal
from models import Call, Transcript, Prediction
from stt import transcribe_audio
from classifier import classify_text

# Create tables automatically if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smartnode Call Classifier",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Smartnode Call Classifier API Running"
    }


@app.post("/analyze")
async def analyze_call(file: UploadFile = File(...)):

    db: Session = SessionLocal()

    try:
        # Validate file type
        allowed_extensions = [".wav", ".mp3", ".m4a"]

        extension = os.path.splitext(file.filename)[1].lower()

        if extension not in allowed_extensions:
            raise HTTPException(
                status_code=400,
                detail="Only .wav, .mp3 and .m4a files are allowed"
            )

        # Create uploads folder
        os.makedirs("uploads", exist_ok=True)

        # Save uploaded file
        file_path = os.path.join(
            "uploads",
            file.filename
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Save call record
        call = Call(
            filename=file.filename
        )

        db.add(call)
        db.commit()
        db.refresh(call)

        # Convert audio to text
        transcript_text = transcribe_audio(file_path)

        transcript = Transcript(
            call_id=call.id,
            transcript_text=transcript_text
        )

        db.add(transcript)
        db.commit()
        db.refresh(transcript)

        # Classify transcript
        label, confidence = classify_text(transcript_text)

        prediction = Prediction(
            call_id=call.id,
            label=label,
            confidence=confidence
        )

        db.add(prediction)
        db.commit()
        db.refresh(prediction)

        return {
            "success": True,
            "call_id": call.id,
            "filename": file.filename,
            "transcript": transcript_text,
            "prediction": label,
            "confidence": round(confidence, 2)
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        db.close()