"""create car_db table

Revision ID: 609f260f3ddd
Revises: dea2c129263b
Create Date: 2024-04-30 09:27:07.016895

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '609f260f3ddd'
down_revision: str | None = 'dea2c129263b'
branch_labels: str | Sequence[str] | None = None
depends_on: str| Sequence[str]| None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
