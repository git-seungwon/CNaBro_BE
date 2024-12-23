"""empty message

Revision ID: ee597262aeb3
Revises: d793a6e0a024
Create Date: 2024-11-21 20:46:50.983169

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'ee597262aeb3'
down_revision: Union[str, None] = 'd793a6e0a024'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('note', 'score',
               existing_type=mysql.TINYBLOB(),
               type_=sa.LargeBinary(length=2),
               existing_comment='집중 단계를 0~3까지 4단계를 2비트로 표현',
               existing_nullable=False)
    op.drop_constraint('tag_ibfk_1', 'tag', type_='foreignkey')
    op.drop_column('tag', 'note_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tag', sa.Column('note_id', mysql.INTEGER(), autoincrement=False, nullable=False, comment='노트 고유번호'))
    op.create_foreign_key('tag_ibfk_1', 'tag', 'note', ['note_id'], ['id'])
    op.alter_column('note', 'score',
               existing_type=sa.LargeBinary(length=2),
               type_=mysql.TINYBLOB(),
               existing_comment='집중 단계를 0~3까지 4단계를 2비트로 표현',
               existing_nullable=False)
    # ### end Alembic commands ###
