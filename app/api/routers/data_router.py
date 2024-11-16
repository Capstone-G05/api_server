from fastapi import APIRouter
from services.redis_service import get_auger_pivot_angle, get_auger_pivot_angle_max, get_auger_pivot_angle_min, get_auger_fold_angle, get_auger_fold_angle_max, get_auger_fold_angle_min, get_spout_tilt_angle, get_spout_tilt_angle_max, get_spout_tilt_angle_min, get_gate_angle, get_gate_angle_max, get_gate_angle_min, get_spout_rotation_angle, get_spout_rotation_angle_max, get_spout_rotation_angle_min, get_auger_fold_speed, get_auger_pivot_speed, get_auger_rotation_speed, get_auger_tilt_speed, get_gate_speed

router = APIRouter()

#auger
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


#spout
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


@router.get("/spout-rotation-angle")
async def spout_rotation_angle():
    angle = get_spout_rotation_angle()
    return {"spout_rotation_angle": angle}


@router.get("/spout-rotation-angle-max")
async def spout_rotation_angle_max():
    max_angle = get_spout_rotation_angle_max()
    return {"spout_rotation_angle_max": max_angle}


@router.get("/spout-rotation-angle-min")
async def spout_rotation_angle_min():
    min_angle = get_spout_rotation_angle_min()
    return {"spout_rotation_angle_min": min_angle}

#gate
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

#speed reference
@router.get("/auger-pivot-speed-ref")
async def auger_pivot_speed():
    speed = get_auger_pivot_speed()
    return {"auger_pivot_speed_ref": speed}

@router.get("/auger-fold-speed-ref")
async def auger_fold_speed():
    speed = get_auger_fold_speed()
    return {"auger_fold_speed_ref": speed}

@router.get("/auger-tilt-speed-ref")
async def auger_tilt_speed():
    speed = get_auger_tilt_speed()
    return {"auger_tilt_speed_ref": speed}

@router.get("/auger-rotation-speed-ref")
async def auger_rotation_speed():
    speed = get_auger_rotation_speed()
    return {"auger_rotation_speed_ref": speed}

@router.get("/gate-speed-ref")
async def gate_speed():
    speed = get_gate_speed()
    return {"gate_speed_ref": speed}


