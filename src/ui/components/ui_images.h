// Copyright 2019 Shift Cryptosecurity AG
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef _UI_IMAGES_H_
#define _UI_IMAGES_H_

#include <stdbool.h>
#include <stdint.h>

#if defined(BOOTLOADER_BTC_ONLY) || defined(FIRMWARE_BTC_ONLY)

#define IMAGE_BB2_LOGO_W 79
#define IMAGE_BB2_LOGO_H 24

static const uint8_t IMAGE_BB2_LOGO[] = {
    0xfe, 0x0c, 0x30, 0x7f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xfe, 0x18, 0x60, 0xff, 0x00, 0x00,
    0x00, 0x07, 0x80, 0xf3, 0x06, 0x00, 0xc1, 0x83, 0x00, 0x00, 0x00, 0x10, 0x82, 0x16, 0x0c, 0x67,
    0xe3, 0x06, 0x0f, 0x87, 0x1c, 0x21, 0x08, 0x1c, 0x18, 0xcf, 0xc6, 0x0c, 0x3f, 0x86, 0x30, 0x81,
    0x00, 0x3f, 0xe1, 0x86, 0x0f, 0xf0, 0x63, 0x06, 0xc1, 0x02, 0x00, 0x7f, 0xc3, 0x0c, 0x1f, 0xe1,
    0x83, 0x0f, 0x82, 0x04, 0x01, 0x60, 0xc6, 0x18, 0x30, 0x63, 0x06, 0x0e, 0x04, 0x08, 0x0c, 0xc1,
    0x8c, 0x30, 0x60, 0xc6, 0x0c, 0x1c, 0x08, 0x10, 0x61, 0x83, 0x18, 0x60, 0xc1, 0x8c, 0x18, 0x7c,
    0x10, 0x21, 0x03, 0x06, 0x30, 0xc1, 0x83, 0x0c, 0x60, 0xd8, 0x10, 0x84, 0x07, 0xf8, 0x61, 0xe3,
    0xfc, 0x1f, 0xc3, 0x18, 0x21, 0x08, 0x0f, 0xe0, 0xc1, 0xc7, 0xf0, 0x1f, 0x0e, 0x38, 0x3c, 0x1f,
    0xe0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x72, 0x00, 0x02, 0x00, 0x00, 0x10, 0x00, 0x05, 0x04, 0x00, 0x90, 0x80,
    0x00, 0x00, 0x00, 0x20, 0x00, 0x08, 0x40, 0x01, 0x2b, 0x98, 0xcb, 0x80, 0xce, 0x51, 0x0c, 0x75,
    0xd3, 0x3b, 0xd2, 0x4a, 0x54, 0x82, 0x52, 0xa2, 0x25, 0x29, 0x29, 0x4c, 0xa4, 0x84, 0xa9, 0x04,
    0xa5, 0x28, 0x7a, 0x52, 0x52, 0x99, 0x49, 0x29, 0x52, 0x09, 0x4a, 0x50, 0x84, 0xa4, 0xa5, 0x3c,
    0x91, 0x8c, 0xa4, 0x0c, 0x94, 0x40, 0xe7, 0x49, 0x32, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00};

#else

#define IMAGE_BB2_LOGO_W 79
#define IMAGE_BB2_LOGO_H 13

static const uint8_t IMAGE_BB2_LOGO[] = {
    0xfe, 0x0c, 0x30, 0x7f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xfe, 0x18, 0x60, 0xff, 0x00,
    0x00, 0x00, 0x07, 0x80, 0xf3, 0x06, 0x00, 0xc1, 0x83, 0x00, 0x00, 0x00, 0x10, 0x82, 0x16,
    0x0c, 0x67, 0xe3, 0x06, 0x0f, 0x87, 0x1c, 0x21, 0x08, 0x1c, 0x18, 0xcf, 0xc6, 0x0c, 0x3f,
    0x86, 0x30, 0x81, 0x00, 0x3f, 0xe1, 0x86, 0x0f, 0xf0, 0x63, 0x06, 0xc1, 0x02, 0x00, 0x7f,
    0xc3, 0x0c, 0x1f, 0xe1, 0x83, 0x0f, 0x82, 0x04, 0x01, 0x60, 0xc6, 0x18, 0x30, 0x63, 0x06,
    0x0e, 0x04, 0x08, 0x0c, 0xc1, 0x8c, 0x30, 0x60, 0xc6, 0x0c, 0x1c, 0x08, 0x10, 0x61, 0x83,
    0x18, 0x60, 0xc1, 0x8c, 0x18, 0x7c, 0x10, 0x21, 0x03, 0x06, 0x30, 0xc1, 0x83, 0x0c, 0x60,
    0xd8, 0x10, 0x84, 0x07, 0xf8, 0x61, 0xe3, 0xfc, 0x1f, 0xc3, 0x18, 0x21, 0x08, 0x0f, 0xe0,
    0xc1, 0xc7, 0xf0, 0x1f, 0x0e, 0x38, 0x3c, 0x1f, 0xe0};

#endif

#define IMAGE_ROTATE_W 22
#define IMAGE_ROTATE_H 14

static const uint8_t IMAGE_ROTATE[] = {0x00, 0x60, 0x00, 0x06, 0x00, 0x00, 0x20, 0x04, 0x01, 0x00,
                                       0x38, 0x04, 0x01, 0xf0, 0x20, 0x0f, 0xe0, 0x80, 0x7f, 0xc2,
                                       0x00, 0x10, 0x08, 0x00, 0x40, 0x10, 0x02, 0x00, 0x40, 0x08,
                                       0x00, 0x80, 0x40, 0x01, 0x86, 0x00, 0x01, 0xe0, 0x00};

static const uint8_t IMAGE_ROTATE_REVERSE[] = {
    0x00, 0x78, 0x00, 0x06, 0x18, 0x00, 0x20, 0x10, 0x01, 0x00, 0x20, 0x04, 0x00,
    0x80, 0x20, 0x01, 0x00, 0x80, 0x04, 0x3f, 0xe0, 0x10, 0x7f, 0x00, 0x40, 0xf8,
    0x02, 0x01, 0xc0, 0x08, 0x02, 0x00, 0x40, 0x00, 0x06, 0x00, 0x00, 0x60, 0x00};

#define IMAGE_DEFAULT_ARROW_HEIGHT 6
#define IMAGE_DEFAULT_CHECKMARK_HEIGHT 5
#define IMAGE_DEFAULT_CROSS_HEIGHT 5
#define IMAGE_DEFAULT_LOCK_RADIUS 6

typedef enum {
    ARROW_RIGHT,
    ARROW_LEFT,
    ARROW_UP,
    ARROW_DOWN,
} arrow_orientation_t;

void image_arrow(int x, int y, int height, arrow_orientation_t orientation);
void image_checkmark(int x, int y, int h);
void image_cross(int x, int y, int h);
void image_lock(int x, int y, int r);
void image_unlock(int x, int y, int r);
void image_sdcard(bool mirror);

#endif
