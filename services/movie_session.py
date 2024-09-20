from django.db.models import QuerySet
from datetime import datetime
from db.models import MovieSession


def create_movie_session(
    movie_show_time: datetime, movie_id: int, cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time, cinema_hall_id=cinema_hall_id, movie_id=movie_id
    )


def get_movies_sessions(session_date: datetime = None) -> QuerySet:
    if session_date:
        year, month, day = session_date.split("-")
        session_datetime = datetime(int(year), int(month), int(day))
        return MovieSession.objects.filter(show_time__date=session_datetime)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None,
) -> MovieSession:
    if show_time:
        MovieSession.objects.filter(id=session_id).update(show_time=show_time)
    if movie_id:
        MovieSession.objects.filter(id=session_id).update(movie_id=movie_id)
    if cinema_hall_id:
        MovieSession.objects.filter(id=session_id).update(cinema_hall_id=cinema_hall_id)
    return MovieSession.objects.filter(id=session_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()