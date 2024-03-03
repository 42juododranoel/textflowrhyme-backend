import typing as t
from abc import ABCMeta, abstractmethod

ProcessedResult = t.TypeVar("ProcessedResult")


class Processor(t.Generic[ProcessedResult], metaclass=ABCMeta):
    """Base class for all processors."""

    is_validated = False

    def __init__(self) -> None:
        """Set important attributes here."""

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

    @abstractmethod
    def _run(self) -> ProcessedResult:
        """Run the business logic."""

    def _fail(
        self,
        non_field_errors: list[str] | None = None,
        **kwargs: list[str],
    ) -> None:
        """
        Fail and raise an error.

        Examples
        --------
        1. self._fail(["nonfielderror"])
        -> ValueError({"non_field_errors": ["nonfielderror"]})

        2. self._fail(foo=["bar"])
        -> ValueError({"foo": ["bar"]})

        3. self._fail(["nonfielderror"], foo=["bar"])
        -> ValueError({"non_field_errors": ["nonfielderror], "foo": ["bar"]})

        """

        messages = {**kwargs}
        if non_field_errors:
            messages["non_field_errors"] = non_field_errors

        raise ValueError(messages)
