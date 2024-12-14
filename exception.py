import sys
import traceback


class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        _, _, exc_tb = error_details.exc_info()
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.lineno = exc_tb.tb_lineno
        self.error_message = error_message

    def __str__(self):
        return (
            f"Error occurred in python script [{self.file_name}] "
            f"at line number [{self.lineno}] with message: [{self.error_message}]"
        )


if __name__ == "__main__":
    try:
        # Example: Trigger a ZeroDivisionError
        a = 1 / 0

    except Exception as e:
        # Log the full traceback (optional for debugging purposes)
        print("Full Traceback:")
        print(traceback.format_exc())  # Detailed traceback information

        # Raise a custom exception with context
        raise CustomException(e, sys)
