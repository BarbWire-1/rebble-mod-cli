#pragma once
#include <pebble.h>

void date_module_init(Layer *parent_layer);
void date_module_deinit(void);
void date_module_update(struct tm *tick_time);