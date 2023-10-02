"""Postgres tables sqlalchemy model"""
from sqlalchemy import Column
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import Boolean, Integer, Float, String, ARRAY
from sqlalchemy.schema import Index

PGBase = declarative_base()


class TitleAkas(PGBase):  # type: ignore
    """Title akas table"""
    __tablename__ = "title_akas"

    title_id = Column("title_id", String(256), nullable=False, primary_key=True)
    ordering = Column("ordering", Integer, nullable=False, primary_key=True)
    title = Column("title", String(256), nullable=False)
    region = Column("region", String(256), nullable=False)
    language = Column("language", String(256), nullable=False)
    types = Column("types", ARRAY(String(256)), nullable=False)
    attributes = Column("attributes", ARRAY(String(256)), nullable=False)
    is_original_title = Column("is_original_title", Boolean, nullable=False)


Index('title_akas_title_index', TitleAkas.title)


class TitleBasics(PGBase):  # type: ignore
    """Title basics table"""
    __tablename__ = "title_basics"

    tconst = Column("tconst", String(256), nullable=False, primary_key=True)
    title_type = Column("title_type", String(256), nullable=False)
    primary_title = Column("primary_title", String(256), nullable=False)
    original_title = Column("original_title", String(256), nullable=False)
    is_adult = Column("is_adult", Boolean, nullable=False)
    start_year = Column("start_year", Integer, nullable=False)
    end_year = Column("end_year", Integer, nullable=True)
    runtime_minutes = Column("runtime_minutes", Integer, nullable=False)
    genres = Column("genres", ARRAY(String(256)), nullable=False)


Index('title_basics_primary_title_index', TitleBasics.primary_title)


class TitleCrew(PGBase):  # type: ignore
    """Title crew table"""
    __tablename__ = "title_crew"

    tconst = Column("tconst", String(256), nullable=False, primary_key=True)
    directors = Column("directors", ARRAY(String(256)), nullable=False)
    writers = Column("writers", ARRAY(String(256)), nullable=False)


class TitleEpisode(PGBase):  # type: ignore
    """Title episode table"""
    __tablename__ = "title_episode"

    tconst = Column("tconst", String(256), nullable=False, primary_key=True)
    parent_tconst = Column("parent_tconst", String(256), nullable=False)
    season_number = Column("season_number", Integer, nullable=False)
    episode_number = Column("episode_number", Integer, nullable=False)


class TitlePrincipals(PGBase):  # type: ignore
    """Title principals table"""
    __tablename__ = "title_principals"

    tconst = Column("tconst", String(256), nullable=False, primary_key=True)
    ordering = Column("ordering", Integer, nullable=False, primary_key=True)
    nconst = Column("nconst", String(256), nullable=False)
    category = Column("category", String(256), nullable=False)
    job = Column("job", String(512), nullable=True)
    characters = Column("characters", String(512), nullable=True)


class TitleRatings(PGBase):  # type: ignore
    """Title ratings table"""
    __tablename__ = "title_ratings"

    tconst = Column("tconst", String(256), nullable=False, primary_key=True)
    average_rating = Column("average_rating", Float, nullable=False)
    num_votes = Column("num_votes", Integer, nullable=False)


class NameBasics(PGBase):  # type: ignore
    """Name basics table"""
    __tablename__ = "name_basics"

    nconst = Column("nconst", String(256), nullable=False, primary_key=True)
    primary_name = Column("primary_name", String(256), nullable=False)
    birth_year = Column("birth_year", String(256), nullable=False)
    death_year = Column("death_year", String(256), nullable=True)
    primary_profession = Column("primary_profession", ARRAY(String(256)), nullable=False)
    known_for_titles = Column("known_for_titles", ARRAY(String(256)), nullable=False)
