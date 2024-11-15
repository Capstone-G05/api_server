from fastapi import APIRouter
from services.redis_service import get_auger_pivot_angle, get_auger_pivot_angle_max, get_auger_pivot_angle_min, get_auger_fold_angle, get_auger_fold_angle_max, get_auger_fold_angle_min, get_spout_tilt_angle, get_spout_tilt_angle_max, get_spout_tilt_angle_min, get_gate_angle, get_gate_angle_max, get_gate_angle_min

router = APIRouter()

@router.get("/auger-pivot-angle")
async def auger_pivot_angle():
    angle = get_auger_pivot_angle()
    return {"auger_pivot_angle": angle}


@router.get("/auger-pivot-angle-max")
async def auger_pivot_angle_max():
    max_angle = get_auger_pivot_angle_max()
    return {"auger_pivot_angle_max": max_angle}


@router.get("/auger-pivot-angle-min")
async def auger_pivot_angle_min():
    min_angle = get_auger_pivot_angle_min()
    return {"auger_pivot_angle_min": min_angle}


@router.get("/auger-fold-angle")
async def auger_fold_angle():
    angle = get_auger_fold_angle()
    return {"auger_fold_angle": angle}


@router.get("/auger-fold-angle-max")
async def auger_fold_angle_max():
    max_angle = get_auger_fold_angle_max()
    return {"auger_fold_angle_max": max_angle}


@router.get("/auger-fold-angle-min")
async def auger_fold_angle_min():
    min_angle = get_auger_fold_angle_min()
    return {"auger_fold_angle_min": min_angle}



@router.get("/spout-tilt-angle")
async def spout_tilt_angle():
    angle = get_spout_tilt_angle()
    return {"spout_tilt_angle": angle}


@router.get("/spout-tilt-angle-max")
async def spout_tilt_angle_max():
    max_angle = get_spout_tilt_angle_max()
    return {"spout_tilt_angle_max": max_angle}


@router.get("/spout-tilt-angle-min")
async def spout_tilt_angle_min():
    min_angle = get_spout_tilt_angle_min()
    return {"spout_tilt_angle_min": min_angle}


@router.get("/gate-angle")
async def gate_angle():
    angle = get_gate_angle()
    return {"gate_angle": angle}


@router.get("/gate-angle-max")
async def gate_angle_max():
    max_angle = get_gate_angle_max()
    return {"gate_angle_max": max_angle}


@router.get("/gate-angle-min")
async def gate_angle_min():
    min_angle = get_gate_angle_min()
    return {"gate_angle_min": min_angle}

