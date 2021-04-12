from typing_extensions import Type

from trench.exceptions import MFAMethodDoesNotExistError
from trench.models import MFAMethod
from trench.utils import get_mfa_model


class IsMFAMethodPrimaryQuery:
    def __init__(self, mfa_model: Type[MFAMethod]):
        self._mfa_model = mfa_model

    def execute(self, user_id: int, name: str) -> bool:
        is_primary = (
            self._mfa_model.objects.filter(user_id=user_id, name=name)
            .values_list("is_primary", flat=True)
            .first()
        )
        if is_primary is None:
            raise MFAMethodDoesNotExistError()
        return is_primary


is_mfa_method_primary_query = IsMFAMethodPrimaryQuery(mfa_model=get_mfa_model()).execute
