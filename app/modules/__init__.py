from .accessmanager import access_manager_app as access_app
from .studentmanager import student_manager_app as student_app
from .trainermanager import trainer_manager_app as trainer_app
from .batchmanager import batch_manager_app as batch_app
from .institutemanager import institute_manager_app as institute_app
from .attendancemanager import attendance_manager_app as attendance_app
from .feesmanager import fees_manager_app as fees_app
from fastapi import APIRouter, Depends

router = APIRouter()
router.include_router(access_app)
router.include_router(student_app, prefix="/manager")
router.include_router(trainer_app, prefix="/manager")
router.include_router(batch_app, prefix="/manager")
router.include_router(institute_app, prefix="/manager")
router.include_router(attendance_app, prefix="/manager")
router.include_router(fees_app, prefix="/manager")

__all__ = [router]
