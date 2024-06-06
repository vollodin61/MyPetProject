from pydantic import BaseModel


class PydProductTypes(BaseModel):
    course: str| None = "course"
    webinar_series: str| None = "webinar_series"
    poll: str| None = "poll"
    otz: str| None = "otz"
    club: str| None = "club"


class PydProductStatuses(BaseModel):
    active: str | None = "active"
    inactive: str | None = "inactive"


class PydCreateProduct(BaseModel):
    name: str | None = ""
    product_type: str | None = PydProductTypes
    price: int | None = None
    status: str | None = PydProductStatuses
    description: str | None = ""

    class Config:
        from_attributes = True
