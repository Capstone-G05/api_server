import time

from fastapi import APIRouter, HTTPException
from fastapi_utils.cbv import cbv

from utils.parameters import Parameter as P
from utils.models import StringTypeRequest, FloatTypeRequest
from services.redis_service import RedisService
from services.sqlite_service import SQLiteService

router = APIRouter()


@cbv(router)
class DataRouter:
    ui_parameters = {}
    frontend_parameters = {}

    def __init__(self):
        self.datastore = RedisService()
        # Note: SQLiteService cannot be shared between threads

    def safe_get(self, parameter: P, datatype: type) -> {}:
        try:
            val = self.datastore.get(parameter.name)
            return {parameter.name: datatype(val) if val is not None else None}
        except ValueError as e:
            raise HTTPException(status_code=404, detail=f"{parameter.name} ValueError: {e}")

    def safe_set(self, parameter: P, value, datatype: type, persist: bool = False) -> {}:
        try:
            value = datatype(value)
            self.datastore.set(parameter.name, value)
            if persist:
                database = SQLiteService()
                database.persist(parameter.name, value)
                database.close()
            return {parameter.name: value}
        except ValueError as e:
            raise HTTPException(status_code=404, detail=f"{parameter.name} ValueError: {e}")

    # PIVOT

    @router.get("/pivot-angle", tags=["pivot"])
    async def get_pivot_angle(self) -> {}:
        return self.safe_get(P.PIVOT_ANGLE, float)

    @router.post("/pivot-angle", tags=["pivot"])
    async def set_pivot_angle(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.PIVOT_ANGLE, request.value, request.datatype, persist=False)

    @router.get("/pivot-angle-max", tags=["pivot"])
    async def get_pivot_angle_max(self) -> {}:
        return self.safe_get(P.PIVOT_ANGLE_MAX, float)

    @router.post("/pivot-angle-max", tags=["pivot"])
    async def set_pivot_angle_max(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.PIVOT_ANGLE_MAX, request.value, request.datatype, persist=True)

    @router.get("/pivot-angle-min", tags=["pivot"])
    async def get_pivot_angle_min(self) -> {}:
        return self.safe_get(P.PIVOT_ANGLE_MIN, float)

    @router.post("/pivot-angle-min", tags=["pivot"])
    async def set_pivot_angle_min(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.PIVOT_ANGLE_MIN, request.value, request.datatype, persist=True)

    @router.get("/pivot-speed-reference", tags=["pivot"])
    async def get_pivot_speed_reference(self) -> {}:
        return self.safe_get(P.PIVOT_SPEED_REFERENCE, float)

    @router.post("/pivot-speed-reference", tags=["pivot"])
    async def set_pivot_speed_reference(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.PIVOT_SPEED_REFERENCE, request.value, request.datatype, persist=True)

    @router.get("/pivot-up-pwm", tags=["pivot"])
    async def get_pivot_up_pwm(self) -> {}:
        return self.safe_get(P.PIVOT_UP_PWM, float)

    @router.get("/pivot-down-pwm", tags=["pivot"])
    async def get_pivot_down_pwm(self) -> {}:
        return self.safe_get(P.PIVOT_DOWN_PWM, float)

    # FOLD

    @router.get("/fold-angle", tags=["fold"])
    async def get_fold_angle(self) -> {}:
        return self.safe_get(P.FOLD_ANGLE, float)

    @router.post("/fold-angle", tags=["fold"])
    async def set_fold_angle(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.FOLD_ANGLE, request.value, request.datatype, persist=False)

    @router.get("/fold-angle-max", tags=["fold"])
    async def get_fold_angle_max(self) -> {}:
        return self.safe_get(P.FOLD_ANGLE_MAX, float)

    @router.post("/fold-angle-max", tags=["fold"])
    async def set_fold_angle_max(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.FOLD_ANGLE_MAX, request.value, request.datatype, persist=True)

    @router.get("/fold-angle-min", tags=["fold"])
    async def get_fold_angle_min(self) -> {}:
        return self.safe_get(P.FOLD_ANGLE_MIN, float)

    @router.post("/fold-angle-min", tags=["fold"])
    async def set_fold_angle_min(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.FOLD_ANGLE_MIN, request.value, request.datatype, persist=True)

    @router.get("/fold-speed-reference", tags=["fold"])
    async def get_fold_speed_reference(self) -> {}:
        return self.safe_get(P.FOLD_SPEED_REFERENCE, float)

    @router.post("/fold-speed-reference", tags=["fold"])
    async def set_fold_speed_reference(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.FOLD_SPEED_REFERENCE, request.value, request.datatype, persist=True)

    @router.get("/fold-out-pwm", tags=["fold"])
    async def get_fold_out_pwm(self) -> {}:
        return self.safe_get(P.FOLD_OUT_PWM, float)

    @router.get("/fold-in-pwm", tags=["fold"])
    async def get_fold_in_pwm(self) -> {}:
        return self.safe_get(P.FOLD_IN_PWM, float)

    # TILT

    @router.get("/tilt-angle", tags=["tilt"])
    async def get_tilt_angle(self) -> {}:
        return self.safe_get(P.TILT_ANGLE, float)

    @router.post("/tilt-angle", tags=["tilt"])
    async def set_tilt_angle(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.TILT_ANGLE, request.value, request.datatype, persist=False)

    @router.get("/tilt-angle-max", tags=["tilt"])
    async def get_tilt_angle_max(self) -> {}:
        return self.safe_get(P.TILT_ANGLE_MAX, float)

    @router.post("/tilt-angle-max", tags=["tilt"])
    async def set_tilt_angle_max(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.TILT_ANGLE_MAX, request.value, request.datatype, persist=True)

    @router.get("/tilt-angle-min", tags=["tilt"])
    async def get_tilt_angle_min(self) -> {}:
        return self.safe_get(P.TILT_ANGLE_MIN, float)

    @router.post("/tilt-angle-min", tags=["tilt"])
    async def set_tilt_angle_min(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.TILT_ANGLE_MIN, request.value, request.datatype, persist=True)

    @router.get("/tilt-speed-reference", tags=["tilt"])
    async def get_tilt_speed_reference(self) -> {}:
        return self.safe_get(P.TILT_SPEED_REFERENCE, float)

    @router.post("/tilt-speed-reference", tags=["tilt"])
    async def set_tilt_speed_reference(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.TILT_SPEED_REFERENCE, request.value, request.datatype, persist=True)

    @router.get("/tilt-up-pwm", tags=["tilt"])
    async def get_tilt_up_pwm(self) -> {}:
        return self.safe_get(P.TILT_UP_PWM, float)

    @router.get("/tilt-down-pwm", tags=["tilt"])
    async def get_tilt_down_pwm(self) -> {}:
        return self.safe_get(P.TILT_DOWN_PWM, float)

    # ROTATE

    @router.get("/rotate-angle", tags=["rotate"])
    async def get_rotate_angle(self) -> {}:
        return self.safe_get(P.ROTATE_ANGLE, float)

    @router.post("/rotate-angle", tags=["rotate"])
    async def set_rotate_angle(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.ROTATE_ANGLE, request.value, request.datatype, persist=False)

    @router.get("/rotate-angle-max", tags=["rotate"])
    async def get_rotate_angle_max(self) -> {}:
        return self.safe_get(P.ROTATE_ANGLE_MAX, float)

    @router.post("/rotate-angle-max", tags=["rotate"])
    async def set_rotate_angle_max(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.ROTATE_ANGLE_MAX, request.value, request.datatype, persist=True)

    @router.get("/rotate-angle-min", tags=["rotate"])
    async def get_rotate_angle_min(self) -> {}:
        return self.safe_get(P.ROTATE_ANGLE_MIN, float)

    @router.post("/rotate-angle-min", tags=["rotate"])
    async def set_rotate_angle_min(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.ROTATE_ANGLE_MIN, request.value, request.datatype, persist=True)

    @router.get("/rotate-speed-reference", tags=["rotate"])
    async def get_rotate_speed_reference(self) -> {}:
        return self.safe_get(P.ROTATE_SPEED_REFERENCE, float)

    @router.post("/rotate-speed-reference", tags=["rotate"])
    async def set_rotate_speed_reference(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.ROTATE_SPEED_REFERENCE, request.value, request.datatype, persist=True)

    @router.get("/rotate-cw-pwm", tags=["rotate"])
    async def get_rotate_cw_pwm(self) -> {}:
        return self.safe_get(P.ROTATE_CW_PWM, float)

    @router.get("/rotate-ccw-pwm", tags=["rotate"])
    async def get_rotate_ccw_pwm(self) -> {}:
        return self.safe_get(P.ROTATE_CCW_PWM, float)

    # GATE

    @router.get("/gate-angle", tags=["gate"])
    async def get_gate_angle(self) -> {}:
        return self.safe_get(P.GATE_ANGLE, float)

    @router.post("/gate-angle", tags=["gate"])
    async def set_gate_angle(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.GATE_ANGLE, request.value, request.datatype, persist=False)

    @router.get("/gate-angle-max", tags=["gate"])
    async def get_gate_angle_max(self) -> {}:
        return self.safe_get(P.GATE_ANGLE_MAX, float)

    @router.post("/gate-angle-max", tags=["gate"])
    async def set_gate_angle_max(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.GATE_ANGLE_MAX, request.value, request.datatype, persist=True)

    @router.get("/gate-angle-min", tags=["gate"])
    async def get_gate_angle_min(self) -> {}:
        return self.safe_get(P.GATE_ANGLE_MIN, float)

    @router.post("/gate-angle-min", tags=["gate"])
    async def set_gate_angle_min(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.GATE_ANGLE_MIN, request.value, request.datatype, persist=True)

    @router.get("/gate-speed-reference", tags=["gate"])
    async def get_gate_speed_reference(self) -> {}:
        return self.safe_get(P.GATE_SPEED_REFERENCE, float)

    @router.post("/gate-speed-reference", tags=["gate"])
    async def set_gate_speed_reference(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.GATE_SPEED_REFERENCE, request.value, request.datatype, persist=True)

    @router.get("/gate-open-pwm", tags=["gate"])
    async def get_gate_open_pwm(self) -> {}:
        return self.safe_get(P.GATE_OPEN_PWM, float)

    @router.get("/gate-close-pwm", tags=["gate"])
    async def get_gate_close_pwm(self) -> {}:
        return self.safe_get(P.GATE_CLOSE_PWM, float)

    # ONLINE (STATUS)

    @router.get("/online", tags=["status"])
    async def get_online(self) -> {}:
        """
        0/65535 = Offline | 1 = Online | 2 = I2C Error | 3 = CAN Error | 4 = OS Error
        """
        return self.safe_get(P.ONLINE, int)

    # USER INPUT

    @router.post("/machine-type", tags=["user_input"])
    async def set_machine_type(self, request: StringTypeRequest) -> {}:
        return self.safe_set(P.MACHINE_TYPE, request.value, request.datatype, persist=False)

    @router.get("/machine-type", tags=["user_input"])
    async def get_machine_type(self) -> {}:
        return self.safe_get(P.MACHINE_TYPE, str)

    @router.post("/crop-fill-rate", tags=["user_input"])
    async def set_crop_fill_rate(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.CROP_FILL_RATE, request.value, request.datatype, persist=True)

    @router.get("/crop-fill-rate", tags=["user_input"])
    async def get_crop_fill_rate(self) -> {}:
        return self.safe_get(P.CROP_FILL_RATE, float)

    @router.post("/pto-flow-rate", tags=["user_input"])
    async def set_pto_flow_rate(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.PTO_FLOW_RATE, request.value, request.datatype, persist=True)

    @router.get("/pto-flow-rate", tags=["user_input"])
    async def get_pto_flow_rate(self) -> {}:
        return self.safe_get(P.PTO_FLOW_RATE, float)

    @router.post("/weight-front", tags=["user_input"])
    async def set_weight_front(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.WEIGHT_FRONT, request.value, request.datatype, persist=False)

    @router.get("/weight-front", tags=["user_input"])
    async def get_weight_front(self) -> {}:
        return self.safe_get(P.WEIGHT_FRONT, float)

    @router.post("/weight-rear", tags=["user_input"])
    async def set_weight_rear(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.WEIGHT_REAR, request.value, request.datatype, persist=False)

    @router.get("/weight-rear", tags=["user_input"])
    async def get_weight_rear(self) -> {}:
        return self.safe_get(P.WEIGHT_REAR, float)

    @router.post("/pto-speed", tags=["user_input"])
    async def set_pto_speed(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.PTO_SPEED, request.value, request.datatype, persist=False)

    @router.get("/pto-speed", tags=["user_input"])
    async def get_pto_speed(self) -> {}:
        return self.safe_get(P.PTO_SPEED, float)

    @router.post("/frame-rate", tags=["user_input"])
    async def set_frame_rate(self, request: FloatTypeRequest) -> {}:
        return self.safe_set(P.FRAME_RATE, request.value, request.datatype, persist=False)
