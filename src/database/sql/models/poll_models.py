from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.database.sql.models.base_model import Base


class Polls(Base):
    __tablename__ = "polls"
    name: Mapped[str | None] = mapped_column(unique=True)
    questions: Mapped[list["Questions"]] = relationship(back_populates="polls", secondary="polls_questions")  # yep
    result: Mapped["Results"] = relationship(back_populates="polls", secondary="polls_results")  # yep


class Questions(Base):
    __tablename__ = "questions"
    text: Mapped[str | None] = mapped_column(unique=True)
    poll: Mapped[list["Polls"]] = relationship(back_populates="questions", secondary="questions_answers")  # yep


class Answers(Base):
    __tablename__ = "answers"
    text: Mapped[str | None] = mapped_column(unique=True)
    question: Mapped[list["Polls"]] = relationship(back_populates="answers", secondary="questions_answers")  # yep


class Results(Base):
    __tablename__ = "results"
    name: Mapped[str | None] = mapped_column(unique=True)
    data: Mapped[str | None] = mapped_column(unique=True)
    poll: Mapped[list["Polls"]] = relationship(back_populates="results", secondary="polls_results")  # yep


class PollsQuestions(Base):
    __tablename__ = "polls_questions"
    poll_id: Mapped[int | None] = mapped_column(ForeignKey("polls.id"))
    question_text: Mapped[str | None] = mapped_column(ForeignKey("questions.text", ondelete="CASCADE"))
    UniqueConstraint("poll_id", name="idx_polls_questions")


class PollsResults(Base):
    __tablename__ = "polls_results"
    poll_id: Mapped[int | None] = mapped_column(ForeignKey("polls.id"))
    result_name: Mapped[str | None] = mapped_column(ForeignKey("results.name", ondelete="CASCADE"))
    result_data: Mapped[str | None] = mapped_column(ForeignKey("results.data", ondelete="CASCADE"))
    UniqueConstraint("poll_id", name="idx_polls_results")


class QuestionsAnswers(Base):
    __tablename__ = "questions_answers"
    question_id: Mapped[int | None] = mapped_column(ForeignKey("questions.id", ondelete="CASCADE"))
    answer_text: Mapped[str | None] = mapped_column(ForeignKey("answers.text", ondelete="CASCADE"))
    UniqueConstraint("question_id", name="idx_questions_answers")
