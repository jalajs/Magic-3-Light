"""empty message

Revision ID: bbd7a2bd503c
Revises: 
Create Date: 2020-01-25 21:38:35.277334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbd7a2bd503c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question_entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=200), nullable=True),
    sa.Column('response', sa.String(length=10), nullable=True),
    sa.Column('time', sa.Time(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question_entry')
    # ### end Alembic commands ###
