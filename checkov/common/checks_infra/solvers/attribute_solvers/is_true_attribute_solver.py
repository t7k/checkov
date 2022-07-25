from typing import Optional, Any, Dict

from checkov.common.graph.checks_infra.enums import Operators
from checkov.common.checks_infra.solvers.attribute_solvers.base_attribute_solver import BaseAttributeSolver


class IsTrueAttributeSolver(BaseAttributeSolver):
    operator = Operators.IS_TRUE  # noqa: CCE003  # a static attribute

    def _get_operation(self, vertex: Dict[str, Any], attribute: Optional[str]) -> bool:  # type:ignore[override]
        attr = vertex.get(attribute)  # type:ignore[arg-type]  # due to attribute can be None
        if attr is None:
            return False

        # if this value contains an underendered variable, then we cannot evaluate the check,
        # so return True (since we cannot return UNKNOWN)
        if self._is_variable_dependant(attr, vertex['source_']):
            return True

        return attr is True