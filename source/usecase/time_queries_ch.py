"""Time various query"""

import logging
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from config.config_ch import CH_CONNECTION_STRING

from data_model.clickhouse_model import TitleAkas, TitleBasics
from source.entities.measure_execution_time import measure_execution_time


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == "__main__":

    engine = create_engine(CH_CONNECTION_STRING)

    with Session(engine) as session:

        # Query examples
        query_on_id = select(TitleBasics).where(TitleBasics.tconst.in_(["tt0000002"]))

        query_title_basics_on_title = select(TitleBasics).where(TitleBasics.primary_title.in_(["La Tosca"]))
        query_title_akas_on_title = select(TitleAkas).where(TitleAkas.title.in_(["La Tosca"]))

        query_join_on_id = select(TitleBasics, TitleAkas).filter(TitleAkas.title_id == TitleBasics.tconst)
        query_join_on_title = select(TitleBasics, TitleAkas).filter(TitleAkas.title == TitleBasics.primary_title)

        query_subset_of_table_columns = select(TitleBasics.primary_title)

        # ## Write your own query and measure execution time ## #

        my_query = query_subset_of_table_columns

        logging.info(f"Executed query: {my_query}")
        result, time_elapsed = measure_execution_time(session, query=my_query)

        # ########################################## #

        logging.info(f"Time elapsed: {time_elapsed}")
