#ifndef Py_OPCODE_H
#define Py_OPCODE_H
#ifdef __cplusplus
extern "C" {
#endif

#include "opcode_ids.h"


#define NB_ADD                                   36
#define NB_AND                                   4
#define NB_FLOOR_DIVIDE                          73
#define NB_LSHIFT                                126
#define NB_MATRIX_MULTIPLY                       123
#define NB_MULTIPLY                              26
#define NB_REMAINDER                             138
#define NB_OR                                    27
#define NB_POWER                                 45
#define NB_RSHIFT                                23
#define NB_SUBTRACT                             121
#define NB_TRUE_DIVIDE                          179
#define NB_XOR                                  55
#define NB_INPLACE_ADD                          202
#define NB_INPLACE_AND                          146
#define NB_INPLACE_FLOOR_DIVIDE                 79
#define NB_INPLACE_LSHIFT                       131
#define NB_INPLACE_MATRIX_MULTIPLY              135
#define NB_INPLACE_MULTIPLY                     138
#define NB_INPLACE_REMAINDER                    115
#define NB_INPLACE_OR                           129
#define NB_INPLACE_POWER                        178
#define NB_INPLACE_RSHIFT                       145
#define NB_INPLACE_SUBTRACT                     64
#define NB_INPLACE_TRUE_DIVIDE                  237
#define NB_INPLACE_XOR                          52

#define NB_OPARG_LAST                           157

#ifdef __cplusplus
}
#endif
#endif /* !Py_OPCODE_H */
