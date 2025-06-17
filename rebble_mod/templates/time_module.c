#include "time_module.h"

static TextLayer *s_time_layer;

void time_module_init(Layer *parent_layer) {
  s_time_layer = text_layer_create(GRect(0, 20, 144, 50));
  text_layer_set_font(s_time_layer, fonts_get_system_font(FONT_KEY_LECO_42_NUMBERS));

  text_layer_set_text_alignment(s_time_layer, GTextAlignmentCenter);
  layer_add_child(parent_layer, text_layer_get_layer(s_time_layer));
}

void time_module_deinit(void) {
  text_layer_destroy(s_time_layer);
}

void time_module_update(struct tm *tick_time) {
  static char buffer[8];
  strftime(buffer, sizeof(buffer), "%H:%M", tick_time);
  text_layer_set_text(s_time_layer, buffer);
}