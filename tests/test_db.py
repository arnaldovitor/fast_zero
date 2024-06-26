from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(
        username='arnaldo', password='secret', email='arnaldo@example.com'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'arnaldo'))

    assert user.username == 'arnaldo'
