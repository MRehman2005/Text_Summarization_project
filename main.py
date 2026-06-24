from textSummarizer.pipeline.stage_1_data_ingestion import DataIngestionTraningPipeLine
from textSummarizer.pipeline.stage_1_data_validation import DataValidationTraningPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME}  Started <<<<<<<")
    data_ingestion = DataIngestionTraningPipeLine()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<<<\n\nx=========x")
    
except Exception  as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data validation Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME}  Started <<<<<<<")
    data_validation = DataValidationTraningPipeline()
    data_validation.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<<<\n\nx=========x")
    
except Exception  as e:
    logger.exception(e)
    raise e