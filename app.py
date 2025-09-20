import argparse
import gc

gc.collect()


ap = argparse.ArgumentParser()

if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()

    from jetpack.log_config import configure_logger

    configure_logger()

    import logging

    from granian import Granian
    from granian.constants import Interfaces

    from scripts.constants.config import Services

    ap.add_argument(
        "--port",
        "-p",
        required=False,
        default=Services.POST,
        help="Port to start the application.",
    )

    ap.add_argument(
        "--host",
        "-H",
        required=False,
        default=Services.HOST,
        help="Host to start the application.",
    )
    arguments = vars(ap.parse_args())
    logging.info(f"Starting the application on {arguments['host']}:{arguments['port']}")
    Granian(
        "main:app",
        address=arguments["host"],
        port=arguments["port"],
        interface=Interfaces.ASGI,
        log_access=True,
    ).serve()
