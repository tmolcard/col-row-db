"""Postgres tables sqlalchemy model"""
from sqlalchemy import Column
from sqlalchemy.orm import declarative_base
from clickhouse_sqlalchemy.types import Boolean, Int, Float, String, Array
from clickhouse_sqlalchemy.engines import MergeTree

# from alembic import context
# from clickhouse_sqlalchemy.alembic.dialect import patch_alembic_version

# pylint: disable=too-few-public-methods

CHBase = declarative_base()


class TitleAkas(CHBase):  # type: ignore
    """Title akas table"""
    __tablename__ = "title_akas"
    __table_args__ = (MergeTree(primary_key='title_id'),)

    title_id = Column("title_id", String(256), primary_key=True)
    ordering = Column("ordering", Int, nullable=False)
    title = Column("title", String(256), nullable=False)
    region = Column("region", String(256), nullable=False)
    language = Column("language", String(256), nullable=False)
    types = Column("types", Array(String(256)), nullable=False)
    attributes = Column("attributes", Array(String(256)), nullable=False)
    is_original_title = Column("is_original_title", Boolean, nullable=False)


class TitleBasics(CHBase):  # type: ignore
    """Title basics table"""
    __tablename__ = "title_basics"
    __table_args__ = (MergeTree(primary_key='tconst'),)

    tconst = Column("tconst", String(256), primary_key=True)
    title_type = Column("title_type", String(256), nullable=False)
    primary_title = Column("primary_title", String(256), nullable=False)
    original_title = Column("original_title", String(256), nullable=False)
    is_adult = Column("is_adult", Boolean, nullable=False)
    start_year = Column("start_year", Int, nullable=False)
    end_year = Column("end_year", Int, nullable=True)
    runtime_minutes = Column("runtime_minutes", Int, nullable=False)
    genres = Column("genres", Array(String(256)), nullable=False)
    MergeTree(primary_key='tconst')


class TitleCrew(CHBase):  # type: ignore
    """Title crew table"""
    __tablename__ = "title_crew"
    __table_args__ = (MergeTree(primary_key='tconst'),)

    tconst = Column("tconst", String(256), primary_key=True)
    directors = Column("directors", Array(String(256)), nullable=False)
    writers = Column("writers", Array(String(256)), nullable=False)


class TitleEpisode(CHBase):  # type: ignore
    """Title episode table"""
    __tablename__ = "title_episode"
    __table_args__ = (MergeTree(primary_key='tconst'),)

    tconst = Column("tconst", String(256), primary_key=True)
    parent_tconst = Column("parent_tconst", String(256), nullable=False)
    season_number = Column("season_number", Int, nullable=False)
    episode_number = Column("episode_number", Int, nullable=False)


class TitlePrincipals(CHBase):  # type: ignore
    """Title principals table"""
    __tablename__ = "title_principals"
    __table_args__ = (MergeTree(primary_key='tconst'),)

    tconst = Column("tconst", String(256), primary_key=True)
    ordering = Column("ordering", Int, nullable=False)
    nconst = Column("nconst", String(256), nullable=False)
    category = Column("category", String(256), nullable=False)
    job = Column("job", String(256), nullable=True)
    characters = Column("characters", String(256), nullable=True)


class TitleRatings(CHBase):  # type: ignore
    """Title ratings table"""
    __tablename__ = "title_ratings"
    __table_args__ = (MergeTree(primary_key='tconst'),)

    tconst = Column("tconst", String(256), primary_key=True)
    average_rating = Column("average_rating", Float, nullable=False)
    num_votes = Column("num_votes", Int, nullable=False)


class NameBasics(CHBase):  # type: ignore
    """Name basics table"""
    __tablename__ = "name_basics"
    __table_args__ = (MergeTree(primary_key='nconst'),)

    nconst = Column("nconst", String(256), primary_key=True)
    primary_name = Column("primary_name", String(256), nullable=False)
    birth_year = Column("birth_year", String(256), nullable=False)
    death_year = Column("death_year", String(256), nullable=True)
    primary_profession = Column("primary_profession", Array(String(256)), nullable=False)
    known_for_titles = Column("known_for_titles", Array(String(256)), nullable=False)
