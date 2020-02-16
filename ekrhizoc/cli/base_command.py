from argparse import ArgumentParser, Namespace


class BaseCommand:
    def __init__(self):
        self.name = ""

    def run(self, args: Namespace):
        self.validate_args(args)

        output = self._execute(args)
        return output

    def add_args(self, parser: ArgumentParser) -> None:
        raise NotImplementedError(
            f"Method: add_args is undefined for command {self.name}"
        )

    def validate_args(self, args: Namespace) -> None:
        raise NotImplementedError(
            f"Method: validate_args is undefined for command {self.name}"
        )

    def _execute(self, args: Namespace):
        try:
            self.execute(args)
        except Exception as ex:
            raise SystemError(ex)

    def execute(self, args: Namespace):
        """Logic of command"""
        raise NotImplementedError(
            f"Method: execute is undefined for command {self.name}"
        )
