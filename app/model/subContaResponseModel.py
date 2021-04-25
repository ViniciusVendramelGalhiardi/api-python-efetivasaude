from datetime import datetime


class Commissions:
    bank_slip_cents: int
    bank_slip_percent: int
    cents: int
    created_at: str
    credit_card_cents: int
    credit_card_percent: int
    id: str
    percent: int
    permit_aggregated: bool
    pix_cents: int
    pix_percent: int
    recipient_account_id: str
    split_id: str
    updated_at: str

    def __init__(self, bank_slip_cents: int, bank_slip_percent: int, cents: int, created_at: datetime, credit_card_cents: int, credit_card_percent: int, id: str, percent: int, permit_aggregated: bool, pix_cents: int, pix_percent: int, recipient_account_id: str, split_id: str, updated_at: datetime) -> None:
        self.bank_slip_cents = bank_slip_cents
        self.bank_slip_percent = bank_slip_percent
        self.cents = cents
        self.created_at = created_at
        self.credit_card_cents = credit_card_cents
        self.credit_card_percent = credit_card_percent
        self.id = id
        self.percent = percent
        self.permit_aggregated = permit_aggregated
        self.pix_cents = pix_cents
        self.pix_percent = pix_percent
        self.recipient_account_id = recipient_account_id
        self.split_id = split_id
        self.updated_at = updated_at


class SubContaResponseModel:
    account_id: str
    name: str
    live_api_token: str
    test_api_token: str
    user_token: str
    commissions: Commissions

    def __init__(self, account_id: str, name: str, live_api_token: str, test_api_token: str, user_token: str, commissions: Commissions) -> None:
        self.account_id = account_id
        self.name = name
        self.live_api_token = live_api_token
        self.test_api_token = test_api_token
        self.user_token = user_token
        self.commissions = commissions