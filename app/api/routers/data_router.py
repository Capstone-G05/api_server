from fastapi import APIRouter, HTTPException
from services.redis_service import get_auger_pivot_angle, get_auger_pivot_angle_max, get_auger_pivot_angle_min, get_auger_fold_angle, get_auger_fold_angle_max, get_auger_fold_angle_min, get_spout_tilt_angle, get_spout_tilt_angle_max, get_spout_tilt_angle_min, get_gate_angle, get_gate_angle_max, get_gate_angle_min, get_spout_rotation_angle, get_spout_rotation_angle_max, get_spout_rotation_angle_min, get_auger_fold_speed, get_auger_pivot_speed, get_spout_rotation_speed, get_spout_tilt_speed, get_gate_speed
from pydantic import BaseModel

router = APIRouter()

ui_parameters = {}

class MachineTypeRequest(BaseModel):
    value: str

class FloatTypeRequest(BaseModel):
    value: float

class PTOTypeRequest(BaseModel):
    value: bool


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

@router.get("/spout-tilt-speed-ref")
async def spout_tilt_speed():
    speed = get_spout_tilt_speed()
    return {"spout_tilt_speed_ref": speed}

@router.get("/spout-rotation-speed-ref")
async def spout_rotation_speed():
    speed = get_spout_rotation_speed()
    return {"spout_rotation_speed_ref": speed}

@router.get("/gate-speed-ref")
async def gate_speed():
    speed = get_gate_speed()
    return {"gate_speed_ref": speed}


# set and get user inputs


@router.post("/set-machine-type")
async def set_machine_type(request: MachineTypeRequest):
    ui_parameters["machine_type"] = request.value
    return {"machine_type": request.value}

@router.get("/machine-type")
async def get_machine_type():
    if "machine_type" not in ui_parameters:
        raise HTTPException(status_code=404, detail="Machine type not set")
    return {"machine_type": ui_parameters["machine_type"]}


@router.post("/set-crop-fill-rate")
async def set_crop_fill_rate(request: FloatTypeRequest):
    ui_parameters["crop_fill_rate"] = request.value
    return {"crop_fill_rate": request.value}

@router.get("/crop-fill-rate")
async def get_crop_fill_rate():
    if "crop_fill_rate" not in ui_parameters:
        raise HTTPException(status_code=404, detail="crop_fill_rate not set")
    return {"crop_fill_rate": ui_parameters["crop_fill_rate"]}

@router.post("/set-front-weight")
async def set_crop_fill_rate(request: FloatTypeRequest):
    ui_parameters["front_weight"] = request.value
    return {"front_weight": request.value}

@router.get("/front-weight")
async def get_crop_fill_rate():
    if "front_weight" not in ui_parameters:
        raise HTTPException(status_code=404, detail="front_weight not set")
    return {"front_weight": ui_parameters["front_weight"]}

@router.post("/set-rear-weight")
async def set_crop_fill_rate(request: FloatTypeRequest):
    ui_parameters["rear_weight"] = request.value
    return {"rear_weight": request.value}

@router.get("/rear-weight")
async def get_crop_fill_rate():
    if "rear_weight" not in ui_parameters:
        raise HTTPException(status_code=404, detail="rear_weight not set")
    return {"rear_weight": ui_parameters["rear_weight"]}


@router.post("/set-pto")
async def set_crop_fill_rate(request: PTOTypeRequest):
    ui_parameters["pto"] = request.value
    return {"pto": request.value}

@router.get("/pto")
async def get_crop_fill_rate():
    if "pto" not in ui_parameters:
        raise HTTPException(status_code=404, detail="pto not set")
    return {"pto": ui_parameters["pto"]}

