"""Utils for retrieving user information."""

import json
from datetime import datetime as dt
from datetime import timezone as tz
from datetime import timedelta

from . import infra_utils


def get_account_age(gh_user):
    cmd = f"gh api users/{gh_user} --jq '{{login, name, created_at}}'"
    account_info = infra_utils.run_cmd(cmd)
    account_info = json.loads(account_info)
    ts_created = dt.fromisoformat(account_info["created_at"])
    return dt.now(tz.utc) - ts_created