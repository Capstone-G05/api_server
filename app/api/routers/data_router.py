from fastapi import APIRouter, HTTPException
<<<<<<< HEAD
from services.redis_service import set_in_redis, get_auger_pivot_angle, get_auger_pivot_angle_max, get_auger_pivot_angle_min, get_auger_top_angle, get_auger_top_angle_max, get_auger_top_angle_min, get_spout_tilt_angle, get_spout_tilt_angle_max, get_spout_tilt_angle_min, get_gate_angle, get_gate_angle_max, get_gate_angle_min, get_head_rotation_angle, get_head_rotation_angle_max, get_head_rotation_angle_min, get_auger_top_speed, get_auger_bottom_pivot_speed, get_head_rotation_speed, get_spout_tilt_speed, get_gate_speed, get_simulation_power, get_auger_pivot_up, get_auger_pivot_down, get_auger_fold, get_auger_unfold, get_spout_tilt_up, get_spout_tilt_down, get_head_rotation_cw, get_head_rotation_ccw, get_gate_open, get_gate_close
=======
from services.redis_service import get_auger_pivot_angle, get_auger_pivot_angle_max, get_auger_pivot_angle_min, get_auger_fold_angle, get_auger_fold_angle_max, get_auger_fold_angle_min, get_spout_tilt_angle, get_spout_tilt_angle_max, get_spout_tilt_angle_min, get_gate_angle, get_gate_angle_max, get_gate_angle_min, get_spout_rotation_angle, get_spout_rotation_angle_max, get_spout_rotation_angle_min, get_auger_fold_speed, get_auger_pivot_speed, get_spout_rotation_speed, get_spout_tilt_speed, get_gate_speed, get_simulation_power
>>>>>>> 86732a364e0ca8d66b28fc00b1af1eb51d6fbcf0
from pydantic import BaseModel

router = APIRouter()

ui_parameters = {}
<<<<<<< HEAD
frontend_parameters ={}
=======
>>>>>>> 86732a364e0ca8d66b28fc00b1af1eb51d6fbcf0

class MachineTypeRequest(BaseModel):
    value: str

class FloatTypeRequest(BaseModel):
    value: float

class PTOTypeRequest(BaseModel):
    value: bool


#auger
<<<<<<< HEAD
@router.get("/auger-bottom-pivot-angle")
async def auger_pivot_angle():
    angle = get_auger_pivot_angle()
    return {"auger_bottom_pivot_angle": angle}


@router.post("/set-auger-bottom-pivot-angle")
async def set_auger_pivot_angle(request: FloatTypeRequest):
    frontend_parameters["auger_bottom_pivot_angle"] = request.value
    set_in_redis("auger_bottom_pivot_angle",str(request.value))
    return {"auger_bottom_pivot_angle": request.value}


@router.post("/set-auger-top-angle")
async def set_auger_top_angle(request: FloatTypeRequest):
    frontend_parameters["auger_top_angle"] = request.value
    set_in_redis("auger_top_angle",str(request.value))
    return {"auger_top_angle": request.value}


@router.post("/set-spout-tilt-angle")
async def set_spout_tilt_angle(request: FloatTypeRequest):
    frontend_parameters["spout_tilt_angle"] = request.value
    set_in_redis("spout_tilt_angle",str(request.value))
    return {"spout_tilt_angle": request.value}



@router.post("/set-head-rotation-angle")
async def set_head_rotation_angle(request: FloatTypeRequest):
    frontend_parameters["head_rotation_angle"] = request.value
    set_in_redis("head_rotation_angle",str(request.value))
    return {"head_rotation_angle": request.value}


@router.post("/set-gate-angle")
async def set_gate_angle(request: FloatTypeRequest):
    frontend_parameters["gate_angle"] = request.value
    set_in_redis("gate_angle",str(request.value))
    return {"gate_angle": request.value}


@router.get("/auger-bottom-pivot-angle-max")
async def auger_pivot_angle_max():
    max_angle = get_auger_pivot_angle_max()
    return {"auger_bottom_pivot_angle_max": max_angle}


@router.get("/auger-bottom-pivot-angle-min")
async def auger_pivot_angle_min():
    min_angle = get_auger_pivot_angle_min()
    return {"auger_bottom_pivot_angle_min": min_angle}


@router.get("/auger-top-angle")
async def auger_top_angle():
    angle = get_auger_top_angle()
    return {"auger_top_angle": angle}


@router.get("/auger-top-angle-max")
async def auger_top_angle_max():
    max_angle = get_auger_top_angle_max()
    return {"auger_top_angle_max": max_angle}


@router.get("/auger-top-angle-min")
async def auger_top_angle_min():
    min_angle = get_auger_top_angle_min()
    return {"auger_top_angle_min": min_angle}
=======
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
>>>>>>> 86732a364e0ca8d66b28fc00b1af1eb51d6fbcf0


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


<<<<<<< HEAD
#head
@router.get("/head-rotation-angle")
async def head_rotation_angle():
    angle = get_head_rotation_angle()
    return {"head_rotation_angle": angle}


@router.get("/head-rotation-angle-max")
async def head_rotation_angle_max():
    max_angle = get_head_rotation_angle_max()
    return {"head_rotation_angle_max": max_angle}


@router.get("/head-rotation-angle-min")
async def head_rotation_angle_min():
    min_angle = get_head_rotation_angle_min()
    return {"head_rotation_angle_min": min_angle}
=======
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
>>>>>>> 86732a364e0ca8d66b28fc00b1af1eb51d6fbcf0

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
<<<<<<< HEAD
@router.get("/auger-bottom-pivot-speed-ref")
async def auger_pivot_speed():
    speed = get_auger_bottom_pivot_speed()
    return {"auger_bottom_pivot_speed_ref": speed}

@router.get("/auger-top-speed-ref")
async def auger_top_speed():
    speed = get_auger_top_speed()
    return {"auger_top_speed_ref": speed}
=======
@router.get("/auger-pivot-speed-ref")
async def auger_pivot_speed():
    speed = get_auger_pivot_speed()
    return {"auger_pivot_speed_ref": speed}

@router.get("/auger-fold-speed-ref")
async def auger_fold_speed():
    speed = get_auger_fold_speed()
    return {"auger_fold_speed_ref": speed}
>>>>>>> 86732a364e0ca8d66b28fc00b1af1eb51d6fbcf0

@router.get("/spout-tilt-speed-ref")
async def spout_tilt_speed():
    speed = get_spout_tilt_speed()
    return {"spout_tilt_speed_ref": speed}

<<<<<<< HEAD
@router.get("/head-rotation-speed-ref")
async def head_rotation_speed():
    speed = get_head_rotation_speed()
    return {"head_rotation_speed_ref": speed}
=======
@router.get("/spout-rotation-speed-ref")
async def spout_rotation_speed():
    speed = get_spout_rotation_speed()
    return {"spout_rotation_speed_ref": speed}
>>>>>>> 86732a364e0ca8d66b28fc00b1af1eb51d6fbcf0

@router.get("/gate-speed-ref")
async def gate_speed():
    speed = get_gate_speed()
    return {"gate_speed_ref": speed}


#simulation power
@router.get("/simulation-power")
async def power():
    power = get_simulation_power()
    return {"simulation_power": power}


#user inputs
@router.post("/set-machine-type")
async def set_machine_type(request: MachineTypeRequest):
    ui_parameters["machine_type"] = request.value
<<<<<<< HEAD
    set_in_redis("machine_type",str(request.value))
=======
>>>>>>> 86732a364e0ca8d66b28fc00b1af1eb51d6fbcf0
    return {"machine_type": request.value}

@router.get("/machine-type")
async def get_machine_type():
    if "machine_type" not in ui_parameters:
        raise HTTPException(status_code=404, detail="Machine type not set")
    return {"machine_type": ui_parameters["machine_type"]}


@router.post("/set-crop-fill-rate")
async def set_crop_fill_rate(request: FloatTypeRequest):
    ui_parameters["crop_fill_rate"] = request.value
<<<<<<< HEAD
    set_in_redis("crop_fill_rate",str(request.value))
=======
>>>>>>> 86732a364e0ca8d66b28fc00b1af1eb51d6fbcf0
    return {"crop_fill_rate": request.value}

@router.get("/crop-fill-rate")
async def get_crop_fill_rate():
    if "crop_fill_rate" not in ui_parameters:
        raise HTTPException(status_code=404, detail="crop_fill_rate not set")
    return {"crop_fill_rate": ui_parameters["crop_fill_rate"]}

@router.post("/set-front-weight")
async def set_crop_fill_rate(request: FloatTypeRequest):
    ui_parameters["front_weight"] = request.value
<<<<<<< HEAD
    set_in_redis("front_weight",str(request.value))
=======
>>>>>>> 86732a364e0ca8d66b28fc00b1af1eb51d6fbcf0
    return {"front_weight": request.value}

@router.get("/front-weight")
async def get_crop_fill_rate():
    if "front_weight" not in ui_parameters:
        raise HTTPException(status_code=404, detail="front_weight not set")
    return {"front_weight": ui_parameters["front_weight"]}

@router.post("/set-rear-weight")
async def set_crop_fill_rate(request: FloatTypeRequest):
    ui_parameters["rear_weight"] = request.value
<<<<<<< HEAD
    set_in_redis("rear_weight",str(request.value))
=======
>>>>>>> 86732a364e0ca8d66b28fc00b1af1eb51d6fbcf0
    return {"rear_weight": request.value}

@router.get("/rear-weight")
async def get_crop_fill_rate():
    if "rear_weight" not in ui_parameters:
        raise HTTPException(status_code=404, detail="rear_weight not set")
    return {"rear_weight": ui_parameters["rear_weight"]}


@router.post("/set-pto")
async def set_crop_fill_rate(request: PTOTypeRequest):
    ui_parameters["pto"] = request.value
<<<<<<< HEAD
    set_in_redis("pto",str(request.value))
=======
>>>>>>> 86732a364e0ca8d66b28fc00b1af1eb51d6fbcf0
    return {"pto": request.value}

@router.get("/pto")
async def get_crop_fill_rate():
    if "pto" not in ui_parameters:
        raise HTTPException(status_code=404, detail="pto not set")
    return {"pto": ui_parameters["pto"]}

<<<<<<< HEAD
#pwm
@router.get("/auger-bottom-pivot-up-pwm")
async def auger_pivot_up():
    pwm = get_auger_pivot_up()
    return {"auger_bottom_pivot_up_pwm": pwm}


@router.get("/auger-bottom-pivot-down-pwm")
async def auger_pivot_down():
    pwm = get_auger_pivot_down()
    return {"auger_bottom_pivot_down_pwm": pwm}


@router.get("/auger-top-fold-pwm")
async def auger_pivot_up():
    pwm = get_auger_fold()
    return {"auger_top_fold_pwm": pwm}


@router.get("/auger-top-unfold-pwm")
async def auger_pivot_down():
    pwm = get_auger_unfold()
    return {"auger_top_unfold_pwm": pwm}


@router.get("/spout-tilt-up-pwm")
async def spout_tilt_up():
    pwm = get_spout_tilt_up()
    return {"spout_tilt_up_pwm": pwm}


@router.get("/spout-tilt-down-pwm")
async def spout_tilt_down():
    pwm = get_spout_tilt_down()
    return {"spout_tilt_down_pwm": pwm}


@router.get("/head-rotation-cw-pwm")
async def head_cw():
    pwm = get_head_rotation_cw()
    return {"head_rotation_cw_pwm": pwm}


@router.get("/head-rotation-ccw-pwm")
async def head_ccw():
    pwm = get_head_rotation_ccw()
    return {"head_rotation_ccw_pwm": pwm}



@router.get("/gate_open-pwm")
async def gate_open():
    pwm = get_gate_open()
    return {"gate_open_pwm": pwm}


@router.get("/gate_close-pwm")
async def gate_close():
    pwm = get_gate_close()
    return {"gate_close_pwm": pwm}







=======
>>>>>>> 86732a364e0ca8d66b28fc00b1af1eb51d6fbcf0
