#pragma once
#include <pebble.h>

void time_module_init(Layer *parent_layer);
void time_module_deinit(void);
void time_module_update(struct tm *tick_time);
