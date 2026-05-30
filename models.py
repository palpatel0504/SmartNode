from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float,
    DateTime,
    ForeignKey
)

from datetime import datetime

from database import Base


class Call(Base):
    __tablename__ = "calls"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(
        String,
        nullable=False
    )

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class Transcript(Base):
    __tablename__ = "transcripts"

    id = Column(Integer, primary_key=True, index=True)

    call_id = Column(
        Integer,
        ForeignKey("calls.id"),
        nullable=False
    )

    transcript_text = Column(
        Text,
        nullable=False
    )


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    call_id = Column(
        Integer,
        ForeignKey("calls.id"),
        nullable=False
    )

    label = Column(
        String,
        nullable=False
    )

    confidence = Column(
        Float,
        nullable=False
    )