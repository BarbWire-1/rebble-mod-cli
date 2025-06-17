#include "date_module.h"

static TextLayer *s_date_layer;

void date_module_init(Layer *parent_layer) {
  s_date_layer = text_layer_create(GRect(0, 70, 144, 30));
  text_layer_set_font(s_date_layer, fonts_get_system_font(FONT_KEY_GOTHIC_24));
  text_layer_set_text_alignment(s_date_layer, GTextAlignmentCenter);
  layer_add_child(parent_layer, text_layer_get_layer(s_date_layer));
}

void date_module_deinit(void) {
  text_layer_destroy(s_date_layer);
}

void date_module_update(struct tm *tick_time) {
  static char buffer[12];
  strftime(buffer, sizeof(buffer), "%a %d %b", tick_time);
  text_layer_set_text(s_date_layer, buffer);
}