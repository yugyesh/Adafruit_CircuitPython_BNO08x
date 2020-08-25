# SPDX-FileCopyrightText: 2020 Bryan Siepert, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
from time import sleep
import board
import busio
from adafruit_bno080.i2c import BNO080_I2C


i2c = busio.I2C(board.SCL, board.SDA)
bno = BNO080_I2C(i2c)

while True:
    print("Rotation Vector Quaternion:")
    quat = bno.quaternion  # pylint:disable=no-member

    print(
        "I: %0.6f  J: %0.6f K: %0.6f  Real: %0.6f" % (quat.i, quat.j, quat.k, quat.real)
    )
    print("")
    print("Acceleration (accelerometer):")
    accel_x, accel_y, accel_z = bno.acceleration  # pylint:disable=no-member
    print("X: %0.6f  Y: %0.6f Z: %0.6f " % (accel_x, accel_y, accel_z))
    print("Linear Acceleration (accelerometer):")
    (
        linear_accel_x,
        linear_accel_y,
        linear_accel_z,
    ) = bno.linear_acceleration  # pylint:disable=no-member
    print(
        "X: %0.6f  Y: %0.6f Z: %0.6f "
        % (linear_accel_x, linear_accel_y, linear_accel_z)
    )
    print("")

    sleep(0.1)
