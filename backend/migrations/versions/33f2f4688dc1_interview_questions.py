"""Interview Questions

Revision ID: 33f2f4688dc1
Revises: 44c2483e2b06
Create Date: 2023-10-13 17:12:50.435280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33f2f4688dc1'
down_revision = '44c2483e2b06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('interview_questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Qn_Id', sa.String(length=9), nullable=False),
    sa.Column('Q_Title', sa.String(length=70), nullable=True),
    sa.Column('Qn_body', sa.Text(), nullable=True),
    sa.Column('IQC_Id', sa.String(length=7), nullable=True),
    sa.Column('reg_at', sa.String(length=100), nullable=False),
    sa.Column('reg_by', sa.String(length=2), nullable=False),
    sa.Column('upd_at', sa.String(length=100), nullable=False),
    sa.Column('upd_by', sa.String(length=2), nullable=False),
    sa.ForeignKeyConstraint(['IQC_Id'], ['question_categories.IQC_ID'], ),
    sa.ForeignKeyConstraint(['reg_by'], ['admins.A_Id'], ),
    sa.ForeignKeyConstraint(['upd_by'], ['admins.A_Id'], ),
    sa.PrimaryKeyConstraint('Qn_Id'),
    sa.UniqueConstraint('Qn_body'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('interview_questions')
    # ### end Alembic commands ###
