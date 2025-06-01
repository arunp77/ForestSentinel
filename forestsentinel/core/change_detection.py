"""
Identifies vegetation changes over time
"""
from pyspark.sql import functions as F

class ChangeDetector:
    def __init__(self, spark_session):
        self.spark = spark_session
        
    def detect_breaks(self, df):
        """Identify statistically significant changes"""
        return df.withColumn("change_flag", 
            F.when(F.abs(F.col("ndvi_diff")) > 0.15, 1).otherwise(0)
        )
