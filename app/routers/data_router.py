import time

from fastapi import APIRouter, HTTPException
from fastapi_utils.cbv import cbv

from utils.parameters import Parameter as P
from services.redis_service import RedisService
from services.sqlite_service import SQLiteService

router = APIRouter()


@cbv(router)
class DataRouter:
    ui_parameters = {}
    frontend_parameters = {}

    def __init__(self):
        self.datastore = RedisService()
        database = SQLiteService()
        database.initialize_database()
        self.datastore.load_data(database)
        database.close()

    # TEST

    @router.get("/test", tags=["test"])
    async def test(self):
        # Test Redis
        print(P.TEST.name)

        self.datastore.set(P.TEST.name, 0)
        redis_start = time.time_ns()
        self.datastore.set(P.TEST.name, 1)
        redis_result = int(self.datastore.get(P.TEST.name)) == 1
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
                "status": "ONLINE" if redis_result else "OFFLINE",
                "delay": (redis_end - redis_start) / 1000000,
            },
            "sqlite": {
                "status": "ONLINE" if sqlite_result else "OFFLINE",
                "delay": (sqlite_end - sqlite_start) / 1000000,
            }
        }

    # PIVOT

    @router.get("/pivot-angle", tags=["pivot"])
    async def get_pivot_angle(self):
        val = self.datastore.get(P.PIVOT_ANGLE.name)
        return float(val) if val is not None else None

    @router.get("/pivot-angle-max", tags=["pivot"])
    async def get_pivot_angle_max(self):
        val = self.datastore.get(P.PIVOT_ANGLE_MAX.name)
        return float(val) if val is not None else None

    @router.get("/pivot-angle-min", tags=["pivot"])
    async def get_pivot_angle_min(self):
        val = self.datastore.get(P.PIVOT_ANGLE_MIN.name)
        return float(val) if val is not None else None

    @router.post("/pivot-angle", tags=["pivot"])
    async def set_pivot_angle(self, value):
        self.datastore.set(P.PIVOT_ANGLE.name, value)
        return value

    @router.get("/pivot-speed-reference", tags=["pivot"])
    async def get_pivot_speed_reference(self):
        val = self.datastore.get(P.PIVOT_SPEED_REFERENCE.name)
        return float(val) if val is not None else None

    @router.get("/pivot-up-pwm", tags=["pivot"])
    async def get_pivot_up_pwm(self):
        val = self.datastore.get(P.PIVOT_UP_PWM.name)
        return float(val) if val is not None else None

    @router.get("/pivot-down-pwm", tags=["pivot"])
    async def get_pivot_down_pwm(self):
        val = self.datastore.get(P.PIVOT_DOWN_PWM.name)
        return float(val) if val is not None else None

    # FOLD

    @router.get("/fold-angle", tags=["fold"])
    async def get_fold_angle(self):
        val = self.datastore.get(P.FOLD_ANGLE.name)
        return float(val) if val is not None else None

    @router.get("/fold-angle-max", tags=["fold"])
    async def get_fold_angle_max(self):
        val = self.datastore.get(P.FOLD_ANGLE_MAX.name)
        return float(val) if val is not None else None

    @router.get("/fold-angle-min", tags=["fold"])
    async def get_fold_angle_min(self):
        val = self.datastore.get(P.FOLD_ANGLE_MIN.name)
        return float(val) if val is not None else None

    @router.post("/fold-angle", tags=["fold"])
    async def set_fold_angle(self, value):
        self.datastore.set(P.FOLD_ANGLE.name, value)
        return value

    @router.get("/fold-speed-reference", tags=["fold"])
    async def get_fold_speed_reference(self):
        val = self.datastore.get(P.FOLD_SPEED_REFERENCE.name)
        return float(val) if val is not None else None

    @router.get("/fold-out-pwm", tags=["fold"])
    async def get_fold_out_pwm(self):
        val = self.datastore.get(P.FOLD_OUT_PWM.name)
        return float(val) if val is not None else None

    @router.get("/fold-in-pwm", tags=["fold"])
    async def get_fold_in_pwm(self):
        val = self.datastore.get(P.FOLD_IN_PWM.name)
        return float(val) if val is not None else None

    # TILT

    @router.get("/tilt-angle", tags=["tilt"])
    async def get_tilt_angle(self):
        val = self.datastore.get(P.TILT_ANGLE.name)
        return float(val) if val is not None else None

    @router.get("/tilt-angle-max", tags=["tilt"])
    async def get_tilt_angle_max(self):
        val = self.datastore.get(P.TILT_ANGLE_MAX.name)
        return float(val) if val is not None else None

    @router.get("/tilt-angle-min", tags=["tilt"])
    async def get_tilt_angle_min(self):
        val = self.datastore.get(P.TILT_ANGLE_MIN.name)
        return float(val) if val is not None else None

    @router.post("/tilt-angle", tags=["tilt"])
    async def set_tilt_angle(self, value):
        self.datastore.set(P.TILT_ANGLE.name, value)
        return value

    @router.get("/tilt-speed-reference", tags=["tilt"])
    async def get_tilt_speed_reference(self):
        val = self.datastore.get(P.TILT_SPEED_REFERENCE.name)
        return float(val) if val is not None else None

    @router.get("/tilt-up-pwm", tags=["tilt"])
    async def get_tilt_up_pwm(self):
        val = self.datastore.get(P.TILT_UP_PWM.name)
        return float(val) if val is not None else None

    @router.get("/tilt-down-pwm", tags=["tilt"])
    async def get_tilt_down_pwm(self):
        val = self.datastore.get(P.TILT_DOWN_PWM.name)
        return float(val) if val is not None else None

    # ROTATE

    @router.get("/rotate-angle", tags=["rotate"])
    async def get_rotate_angle(self):
        val = self.datastore.get(P.ROTATE_ANGLE.name)
        return float(val) if val is not None else None

    @router.get("/rotate-angle-max", tags=["rotate"])
    async def get_rotate_angle_max(self):
        val = self.datastore.get(P.ROTATE_ANGLE_MAX.name)
        return float(val) if val is not None else None

    @router.get("/rotate-angle-min", tags=["rotate"])
    async def get_rotate_angle_min(self):
        val = self.datastore.get(P.ROTATE_ANGLE_MIN.name)
        return float(val) if val is not None else None

    @router.post("/rotate-angle", tags=["rotate"])
    async def set_rotate_angle(self, value):
        self.datastore.set(P.ROTATE_ANGLE.name, value)
        return value

    @router.get("/rotate-speed-reference", tags=["rotate"])
    async def get_rotate_speed_reference(self):
        val = self.datastore.get(P.ROTATE_SPEED_REFERENCE.name)
        return float(val) if val is not None else None

    @router.get("/rotate-cw-pwm", tags=["rotate"])
    async def get_rotate_cw_pwm(self):
        val = self.datastore.get(P.ROTATE_CW_PWM.name)
        return float(val) if val is not None else None

    @router.get("/rotate-ccw-pwm", tags=["rotate"])
    async def get_rotate_ccw_pwm(self):
        val = self.datastore.get(P.ROTATE_CCW_PWM.name)
        return float(val) if val is not None else None

    # GATE

    @router.get("/gate-angle", tags=["gate"])
    async def get_gate_angle(self):
        val = self.datastore.get(P.GATE_ANGLE.name)
        return float(val) if val is not None else None

    @router.get("/gate-angle-max", tags=["gate"])
    async def get_gate_angle_max(self):
        val = self.datastore.get(P.GATE_ANGLE_MAX.name)
        return float(val) if val is not None else None

    @router.get("/gate-angle-min", tags=["gate"])
    async def get_gate_angle_min(self):
        val = self.datastore.get(P.GATE_ANGLE_MIN.name)
        return float(val) if val is not None else None

    @router.post("/gate-angle", tags=["gate"])
    async def set_gate_angle(self, value):
        self.datastore.set(P.GATE_ANGLE.name, value)
        return value

    @router.get("/gate-speed-reference", tags=["gate"])
    async def get_gate_speed_reference(self):
        val = self.datastore.get(P.GATE_SPEED_REFERENCE.name)
        return float(val) if val is not None else None

    @router.get("/gate-open-pwm", tags=["gate"])
    async def get_gate_open_pwm(self):
        val = self.datastore.get(P.GATE_OPEN_PWM.name)
        return float(val) if val is not None else None

    @router.get("/gate-close-pwm", tags=["gate"])
    async def get_gate_close_pwm(self):
        val = self.datastore.get(P.GATE_CLOSE_PWM.name)
        return float(val) if val is not None else None

    # ONLINE (STATUS)

    @router.get("/online")
    async def get_online(self):
        val = self.datastore.get(P.ONLINE.name)
        return int(val) if val is not None else None

    # USER INPUT

    @router.post("/machine-type", tags=["user_input"])
    async def set_machine_type(self, value):
        self.datastore.set(P.MACHINE_TYPE.name, value)
        return value

    @router.get("/machine-type", tags=["user_input"])
    async def get_machine_type(self):
        val = self.datastore.get(P.MACHINE_TYPE.name)
        return str(val) if val is not None else None

    @router.post("/crop-fill-rate", tags=["user_input"])
    async def set_crop_fill_rate(self, value):
        self.datastore.set(P.CROP_FILL_RATE.name, value)
        return value

    @router.get("/crop-fill-rate", tags=["user_input"])
    async def get_crop_fill_rate(self):
        val = self.datastore.get(P.CROP_FILL_RATE.name)
        return float(val) if val is not None else None

    @router.post("/weight-front", tags=["user_input"])
    async def set_weight_front(self, value):
        self.datastore.set(P.WEIGHT_FRONT.name, value)
        return value

    @router.get("/weight-front", tags=["user_input"])
    async def get_weight_front(self):
        val = self.datastore.get(P.WEIGHT_FRONT.name)
        return float(val) if val is not None else None

    @router.post("/weight-rear", tags=["user_input"])
    async def set_weight_rear(self, value):
        self.datastore.set(P.WEIGHT_REAR.name, value)
        return value

    @router.get("/weight-rear", tags=["user_input"])
    async def get_weight_rear(self):
        val = self.datastore.get(P.WEIGHT_REAR.name)
        return float(val) if val is not None else None

    @router.post("/pto-speed", tags=["user_input"])
    async def set_pto_speed(self, value):
        self.datastore.set(P.PTO_SPEED.name, value)
        return value

    @router.get("/pto-speed", tags=["user_input"])
    async def get_pto_speed(self):
        val = self.datastore.get(P.PTO_SPEED.name)
        return float(val) if val is not None else None
