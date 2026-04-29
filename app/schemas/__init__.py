from pydantic import BaseModel
from typing import Optional, Dict

class ProjectRequest(BaseModel):
    project_name: str
    description: str
    vibe_override: Optional[Dict] = None

class ProjectResponse(BaseModel):
    project_name: str
    structure_preview: list
    status: str
    message: str