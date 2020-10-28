from typing import Union, List

from .db import db
from .models import LinksPair


def create_links_pair(original_url: str, days_limit: Union[int, None]) -> LinksPair:
    new_links_pair = LinksPair(original_url=original_url,
                               days_limit=days_limit)

    db.session.add(new_links_pair)
    db.session.commit()

    return new_links_pair


def get_links_pair(pair_id: int) -> LinksPair:
    db_entry = LinksPair.query.filter_by(id=pair_id).first_or_404(
        description=f"Object with 'id': {pair_id} does not exist.")
    return db_entry


def get_links_pair_by_short_url(short_url: int) -> LinksPair:
    db_entry = LinksPair.query.filter_by(short_url=short_url).first_or_404(
        description=f"Object with 'short_url': {short_url} does not exist.")
    return db_entry


def get_all_links_pairs() -> List[LinksPair]:
    db_entries = LinksPair.query.all()
    return db_entries


def update_links_pair():
    pass


def delete_links_pair(pair_id: int) -> LinksPair:
    db_entry = LinksPair.query.filter_by(id=pair_id).first_or_404(
        description=f"Object with 'id': {pair_id} does not exist.")

    db.session.delete(db_entry)
    db.session.commit()

    return db_entry
