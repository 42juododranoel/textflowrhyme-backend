import typing

ProcessedResult = typing.TypeVar("ProcessedResult")


class Processor(typing.Generic[ProcessedResult]):
    """Base class for all processors."""

    is_validated = False

    def run(self) -> ProcessedResult:
        """Validate if not validated already and run the business logic."""

        if not self.is_validated:
            self.validate()

        return self._run()

    def validate(self) -> None:
        """Validate and set the flag."""

        self._validate()
        self.is_validated = True

    def _validate(self) -> None:
        """Validate the input data before running."""

    def _run(self) -> ProcessedResult:
        """Run the business logic."""

    def _fail(
        self,
        non_field_errors: list[str] | None = None,
        **kwargs: dict[str, list[str]],
    ) -> None:
        """
        Fail and raise an error.

        Examples
        --------
        1. self._fail(["foobar"])
        -> ValueError({"non_field_errors": ["foobar"]})

        2. self._fail(foo=["bar"])
        -> ValueError({"foo": ["bar"]})

        3. self._fail(["foobar"], foo=["bar"])
        -> ValueError({"non_field_errors": ["foobar], "foo": ["bar"]})

        """

        messages = {**kwargs}
        if non_field_errors:
            messages["non_field_errors"] = non_field_errors

        raise ValueError(messages)
