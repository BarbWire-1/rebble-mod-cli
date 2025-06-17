#include <pebble.h>
#include "../../modules_pool/time_module.h"
#include "../../modules_pool/date_module.h"

static Window *s_main_window;

static void tick_handler(struct tm *tick_time, TimeUnits units_changed) {
  time_module_update(tick_time);
  date_module_update(tick_time);
}

static void main_window_load(Window *window) {
  Layer *window_layer = window_get_root_layer(window);
  time_module_init(window_layer);
  date_module_init(window_layer);
}

static void main_window_unload(Window *window) {
  time_module_deinit();
  date_module_deinit();
}

static void init(void) {
  s_main_window = window_create();

  window_set_window_handlers(s_main_window, (WindowHandlers){
    .load = main_window_load,
    .unload = main_window_unload,
  });

  window_stack_push(s_main_window, true);

  tick_timer_service_subscribe(MINUTE_UNIT, tick_handler);

  // Initialize display immediately with current time/date
  time_t now = time(NULL);
  struct tm *tick_time = localtime(&now);
  time_module_update(tick_time);
  date_module_update(tick_time);
}

static void deinit(void) {
  tick_timer_service_unsubscribe();
  window_destroy(s_main_window);
}

int main(void) {
  init();
  app_event_loop();
  deinit();
}