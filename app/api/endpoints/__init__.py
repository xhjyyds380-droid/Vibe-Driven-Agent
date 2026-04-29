from fastapi import APIRouter, HTTPException
from app.schemas.project import ProjectRequest, ProjectResponse
from app.services.architect_service import ArchitectService

router = APIRouter()
service = ArchitectService()

@router.post("/generate", response_model=ProjectResponse)
async def create_project(request: ProjectRequest):
    try:
        struct, steps = await service.generate_structure(
            request.project_name, 
            request.description
        )
        return ProjectResponse(
            project_name=request.project_name,
            structure_preview=struct,
            status="Success",
            message=f"已完成长链推理：{', '.join(steps)}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))