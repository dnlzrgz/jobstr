from datetime import date
from sqlmodel import Field, Relationship, SQLModel, create_engine
from jobstr.settings import settings


class ApplicationTagLink(SQLModel, table=True):
    application_id: int | None = Field(
        default=None,
        foreign_key="application.id",
        primary_key=True,
    )
    tag_id: int | None = Field(
        default=None,
        foreign_key="tag.id",
        primary_key=True,
    )


class Tag(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True)

    applications: list["Application"] = Relationship(
        back_populates="tags",
        link_model=ApplicationTagLink,
    )


class Company(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    name: str = Field(unique=True)
    website: str | None = None
    industry: str | None = None
    location: str | None = None

    applications: list["Application"] = Relationship(back_populates="company")


class Application(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    company: Company | None = Relationship(back_populates="applications")
    company_id: int | None = Field(default=None, foreign_key="company.id")

    job_title: str
    job_description: str
    job_url: str

    application_date: date

    status: str
    salary_range: str | None = None
    location_type: str = "On-site"

    last_update: date = Field(
        default_factory=date.today,
        sa_column_kwargs={"default": "CURRENT_DATE"},
    )

    notes: str | None = None

    tags: list[Tag] = Relationship(
        back_populates="applications",
        link_model=ApplicationTagLink,
    )


engine = create_engine(settings.db_url)
SQLModel.metadata.create_all(engine)
