from flask import Flask, request
from flask_limiter import Limiter
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

limiter = Limiter(
    app,
    key_func=lambda: request.headers.get("X-Real-Ip"),
)


@app.route("/status_code_please/<status_code>", methods=["GET"])
@cross_origin(support_credentials=True)
@limiter.limit("30 per 7 days")
def status_code_please(status_code):
    try:
        status_code = validate_and_return_properly_parsed_status_code_if_parsing_was_successful_otherwise_raise_one_of_multiple_custom_exceptions_based_on_exception_criteria(
            status_code
        )
    except:
        return "Bad request", 400
    return str(status_code), status_code


def validate_and_return_properly_parsed_status_code_if_parsing_was_successful_otherwise_raise_one_of_multiple_custom_exceptions_based_on_exception_criteria(
    status_code: str,
):
    status_code = int(status_code)
    if status_code <= 0:
        raise StatusCodeNonPositive
    if status_code > 2147483647:
        raise StatusCodeTooLarge

    return status_code


class StatusCodeNonPositive(Exception):
    pass


class StatusCodeTooLarge(Exception):
    pass


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")