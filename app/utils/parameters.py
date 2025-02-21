import enum


class Parameter(enum.StrEnum):
    TEST = "TEST"                                          # unitless
    ONLINE = "ONLINE"                                      # status (1: OK, 2: I2C_ERROR, 3: CAN_ERROR, 4: OS_ERROR)
    MACHINE_TYPE = "MACHINE_TYPE"                          # unitless

    CROP_FILL_RATE = "CROP_FILL_RATE"                      # kg / click
    WEIGHT_FRONT = "WEIGHT_FRONT"                          # kg
    WEIGHT_REAR = "WEIGHT_REAR"                            # kg
    PTO_SPEED = "PTO_SPEED"                                # RPM
    PTO_FLOW_RATE = "PTO_FLOW_RATE"                        # kg / rotation

    PIVOT_ANGLE = "PIVOT_ANGLE"                            # degrees (0-360)
    PIVOT_ANGLE_MAX = "PIVOT_ANGLE_MAX"                    # degrees (0-360)
    PIVOT_ANGLE_MIN = "PIVOT_ANGLE_MIN"                    # degrees (0-360)
    PIVOT_SPEED_REFERENCE = "PIVOT_SPEED_REFERENCE"        # degrees / s
    PIVOT_UP_PWM = "PIVOT_UP_PWM"                          # percent (0-100)
    PIVOT_DOWN_PWM = "PIVOT_DOWN_PWM"                      # percent (0-100)

    FOLD_ANGLE = "FOLD_ANGLE"                              # degrees (0-360)
    FOLD_ANGLE_MAX = "FOLD_ANGLE_MAX"                      # degrees (0-360)
    FOLD_ANGLE_MIN = "FOLD_ANGLE_MIN"                      # degrees (0-360)
    FOLD_SPEED_REFERENCE = "FOLD_SPEED_REFERENCE"          # degrees / s
    FOLD_OUT_PWM = "FOLD_OUT_PWM"                          # percent (0-100)
    FOLD_IN_PWM = "FOLD_IN_PWM"                            # percent (0-100)

    TILT_ANGLE = "TILT_ANGLE"                              # degrees (0-360)
    TILT_ANGLE_MAX = "TILT_ANGLE_MAX"                      # degrees (0-360)
    TILT_ANGLE_MIN = "TILT_ANGLE_MIN"                      # degrees (0-360)
    TILT_SPEED_REFERENCE = "TILT_SPEED_REFERENCE"          # degrees / s
    TILT_UP_PWM = "TILT_UP_PWM"                            # percent (0-100)
    TILT_DOWN_PWM = "TILT_DOWN_PWM"                        # percent (0-100)

    ROTATE_ANGLE = "ROTATE_ANGLE"                          # degrees (0-360)
    ROTATE_ANGLE_MAX = "ROTATE_ANGLE_MAX"                  # degrees (0-360)
    ROTATE_ANGLE_MIN = "ROTATE_ANGLE_MIN"                  # degrees (0-360)
    ROTATE_SPEED_REFERENCE = "ROTATE_SPEED_REFERENCE"      # degrees / s
    ROTATE_CW_PWM = "ROTATE_CW_PWM"                        # percent (0-100)
    ROTATE_CCW_PWM = "ROTATE_CCW_PWM"                      # percent (0-100)

    GATE_ANGLE = "GATE_ANGLE"                              # degrees (0-360)
    GATE_ANGLE_MAX = "GATE_ANGLE_MAX"                      # degrees (0-360)
    GATE_ANGLE_MIN = "GATE_ANGLE_MIN"                      # degrees (0-360)
    GATE_SPEED_REFERENCE = "GATE_SPEED_REFERENCE"          # degrees / s
    GATE_OPEN_PWM = "GATE_OPEN_PWM"                        # percent (0-100)
    GATE_CLOSE_PWM = "GATE_CLOSE_PWM"                      # percent (0-100)

    @property
    def name(self):
        return self.value
