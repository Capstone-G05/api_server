import time

from fastapi import APIRouter, HTTPException
from fastapi_utils.cbv import cbv

from utils.models import StringTypeRequest, FloatTypeRequest, BooleanTypeRequest
from services.redis_service import RedisService
from services.sqlite_service import SQLiteService

router = APIRouter()


@cbv(router)
class DataRouter:
    ui_parameters = {}
    frontend_parameters = {}

    def __init__(self):
        self.datastore = RedisService()
        # note: SQLiteService cannot be shared between route threads
        database = SQLiteService()
        database.initialize_database()
        self.datastore.load_data(database)
        database.close()

    def get_param(self, param: str, datatype: type):
        return {param, self.datastore.get(param, datatype)}

    @staticmethod
    def get_cached_param(group: dict, param: str):
        if param not in group:
            raise HTTPException(status_code=404, detail=f"{param} not set")
        return {param: group[param]}

    def set_param(self, group: dict, param: str, value):
        group[param] = value
        self.datastore.set(param, str(value))
        return {param: value}

    # TEST

    @router.get("/test")
    async def test(self):
        # Test Redis
        self.datastore.set("test", 1)
        redis_start = time.time_ns()
        self.datastore.set("TEST", 1)
        redis_result = self.datastore.get("TEST", int) == 1
        redis_end = time.time_ns()
        # Test SQLite
        database = SQLiteService()
        database.execute("DELETE FROM redis_keys WHERE key = 'test'")
        sqlite_start = time.time_ns()
        database.execute("INSERT INTO redis_keys (key, value) VALUES ('test', 1)")
        cursor = database.execute("SELECT value FROM redis_keys WHERE key = 'test'")
        sqlite_result = int(cursor.fetchone()[0]) == 1
        sqlite_end = time.time_ns()
        database.close()
        # Return test results
        return {
            "redis": {
                "status": "online" if redis_result else "offline",
                "delay": (redis_end - redis_start) / 1000000,
            },
            "sqlite": {
                "status": "online" if sqlite_result else "offline",
                "delay": (sqlite_end - sqlite_start) / 1000000,
            }
        }

    # AUGER BOTTOM

    @router.get("/auger-bottom-pivot-angle")
    async def auger_bottom_pivot_angle(self):
        return self.get_param("auger_bottom_pivot_angle", float)

    @router.get("/auger-bottom-pivot-angle-max")
    async def auger_bottom_pivot_angle_max(self):
        return self.get_param("auger_bottom_pivot_angle_max", float)

    @router.get("/auger-bottom-pivot-angle-min")
    async def auger_bottom_pivot_angle_min(self):
        return self.get_param("auger_bottom_pivot_angle_min", float)

    @router.post("/set-auger-bottom-pivot-angle")
    async def set_auger_bottom_pivot_angle(self, request: FloatTypeRequest):
        return self.set_param(self.frontend_parameters, "auger_bottom_pivot_angle", request.value)

    # AUGER TOP ANGLE

    @router.get("/auger-top-angle")
    async def auger_top_angle(self):
        return self.get_param("auger_top_angle", float)

    @router.get("/auger-top-angle-max")
    async def auger_top_angle_max(self):
        return self.get_param("auger_top_angle_max", float)

    @router.get("/auger-top-angle-min")
    async def auger_top_angle_min(self):
        return self.get_param("auger_top_angle_min", float)

    @router.post("/set-auger-top-angle")
    async def set_auger_top_angle(self, request: FloatTypeRequest):
        return self.set_param(self.frontend_parameters, "auger_top_angle", request.value)

    # SPOUT TILT ANGLE

    @router.get("/spout-tilt-angle")
    async def spout_tilt_angle(self):
        return self.get_param("spout_tilt_angle", float)

    @router.get("/spout-tilt-angle-max")
    async def spout_tilt_angle_max(self):
        return self.get_param("spout_tilt_angle_max", float)

    @router.get("/spout-tilt-angle-min")
    async def spout_tilt_angle_min(self):
        return self.get_param("spout_tilt_angle_min", float)

    @router.post("/set-spout-tilt-angle")
    async def set_spout_tilt_angle(self, request: FloatTypeRequest):
        return self.set_param(self.frontend_parameters, "spout_tilt_angle", request.value)

    # SPOUT HEAD ANGLE

    @router.get("/head-rotation-angle")
    async def head_rotation_angle(self):
        return self.get_param("head_rotation_angle", float)

    @router.get("/head-rotation-angle-max")
    async def head_rotation_angle_max(self):
        return self.get_param("head_rotation_angle_max", float)

    @router.get("/head-rotation-angle-min")
    async def head_rotation_angle_min(self):
        return self.get_param("head_rotation_angle_min", float)

    @router.post("/set-head-rotation-angle")
    async def set_head_rotation_angle(self, request: FloatTypeRequest):
        return self.set_param(self.frontend_parameters, "head_rotation_angle", request.value)

    # GATE ANGLE

    @router.get("/gate-angle")
    async def gate_angle(self):
        return self.get_param("gate_angle", float)

    @router.get("/gate-angle-max")
    async def gate_angle_max(self):
        return self.get_param("gate_angle_max", float)

    @router.get("/gate-angle-min")
    async def gate_angle_min(self):
        return self.get_param("gate_angle_min", float)

    @router.post("/set-gate-angle")
    async def set_gate_angle(self, request: FloatTypeRequest):
        return self.set_param(self.frontend_parameters, "gate_angle", request.value)

    # SPEED REFERENCE

    @router.get("/auger-bottom-pivot-speed-ref")
    async def auger_bottom_pivot_speed_ref(self):
        return self.get_param("auger_bottom_pivot_speed_ref", float)

    @router.get("/auger-top-speed-ref")
    async def auger_top_speed_ref(self):
        return self.get_param("auger_top_speed_ref", float)

    @router.get("/spout-tilt-speed-ref")
    async def spout_tilt_speed_ref(self):
        return self.get_param("spout_tilt_speed_ref", float)

    @router.get("/head-rotation-speed-ref")
    async def head_rotation_speed_ref(self):
        return self.get_param("head_rotation_speed_ref", float)

    @router.get("/gate-speed-ref")
    async def gate_speed_ref(self):
        return self.get_param("gate_speed_ref", float)

    # SIMULATION POWER

    @router.get("/simulation-power")
    async def simulation_power(self):
        status = self.datastore.get("simulation_power", str).lower() == "true"
        return {"simulation_power": status}

    # USER INPUTS

    @router.post("/set-machine-type")
    async def set_machine_type(self, request: StringTypeRequest):
        return self.set_param(self.ui_parameters, "machine_type", request.value)

    @router.get("/machine-type")
    async def get_machine_type(self):
        return self.get_cached_param(self.ui_parameters, "machine_type")

    @router.post("/set-crop-fill-rate")
    async def set_crop_fill_rate(self, request: FloatTypeRequest):
        return self.set_param(self.ui_parameters, "crop_fill_rate", request.value)

    @router.get("/crop-fill-rate")
    async def get_crop_fill_rate(self):
        return self.get_cached_param(self.ui_parameters, "crop_fill_rate")

    @router.post("/set-front-weight")
    async def set_front_weight(self, request: FloatTypeRequest):
        return self.set_param(self.ui_parameters, "front_weight", request.value)

    @router.get("/front-weight")
    async def get_front_weight(self):
        return self.get_cached_param(self.ui_parameters, "front_weight")


    @router.post("/set-rear-weight")
    async def set_rear_weight(self, request: FloatTypeRequest):
        return self.set_param(self.ui_parameters, "rear_weight", request.value)

    @router.get("/rear-weight")
    async def get_rear_weight(self):
        return self.get_cached_param(self.ui_parameters, "rear_weight")

    @router.post("/set-pto")
    async def set_pto(self, request: BooleanTypeRequest):
        return self.set_param(self.ui_parameters, "pto", request.value)

    @router.get("/pto")
    async def get_pto(self):
        return self.get_cached_param(self.ui_parameters, "pto")

    # PWM

    @router.get("/auger-bottom-pivot-up-pwm")
    async def auger_bottom_pivot_up_pwm(self):
        return self.get_param("auger_bottom_pivot_up_pwm", float)

    @router.get("/auger-bottom-pivot-down-pwm")
    async def auger_bottom_pivot_down_pwm(self):
        return self.get_param("auger_bottom_pivot_down_pwm", float)

    @router.get("/auger-top-fold-pwm")
    async def auger_top_fold_pwm(self):
        return self.get_param("auger_top_fold_pwm", float)

    @router.get("/auger-top-unfold-pwm")
    async def auger_top_unfold_pwm(self):
        return self.get_param("auger_top_unfold_pwm", float)

    @router.get("/spout-tilt-up-pwm")
    async def spout_tilt_up_pwm(self):
        return self.get_param("spout_tilt_up_pwm", float)

    @router.get("/spout-tilt-down-pwm")
    async def spout_tilt_down_pwm(self):
        return self.get_param("spout_tilt_down_pwm", float)

    @router.get("/head-rotation-cw-pwm")
    async def head_rotation_cw_pwm(self):
        return self.get_param("head_rotation_cw_pwm", float)

    @router.get("/head-rotation-ccw-pwm")
    async def head_rotation_ccw_pwm(self):
        return self.get_param("head_rotation_ccw_pwm", float)

    @router.get("/gate_open-pwm")
    async def gate_open_pwm(self):
        return self.get_param("gate_open_pwm", float)

    @router.get("/gate_close-pwm")
    async def gate_close_pwm(self):
        return self.get_param("gate_close_pwm", float)
