
from icecream import ic
from init_database import Base_asynconf, asynconf
from sqlalchemy import Column, Integer, String


class LoanRate(Base_asynconf):
    """
    A class used to represent the loan rate.

    Data come from ASYNCONF Hackathon 2023 - Green Bank, Banque Populaire Val de France.
    """
    __tablename__ = "loan_rate"

    id = Column("Id", Integer, primary_key=True)
    score = Column("Score", String)
    rate = Column("Rate", Integer)

    def __init__(self, id, score, rate):
        self.id = id
        self.score = score
        self.rate = rate


def get_loan_rate(score: int) -> float:
    """
    Retrieves loan rate according to the customer ecological score.

    Args:
        score (int): The ecological score of the customer

    Returns:
        int: The loan rate in %.
    """
    query = asynconf.query(LoanRate).filter(LoanRate.score <= score)
    element_object = query.order_by(LoanRate.id.desc()).first()
    if element_object is None:
        raise ValueError(f"An error occured.")
    return element_object.rate


if __name__ == "__main__":
    print(get_loan_rate(score=8))
    print(get_loan_rate(score=11))
    print(get_loan_rate(score=16))
