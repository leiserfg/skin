set(DOXYGEN_SKIP_DOT True)

find_package(Doxygen)

if (DOXYGEN_FOUND)
  message (STATUS "Se ha encontrado Doxygen (${DOXYGEN_EXECUTABLE} ${DOXYGEN_VERSION}) en el sistema, se brinda soporte para la documentación.")

  configure_file(
    "${PROJECT_SOURCE_DIR}/doc/Doxyfile.in"
    "${PROJECT_BINARY_DIR}/doc/Doxyfile"
    @ONLY
  )

  add_custom_target(processinfo-doc
    COMMAND
      ${DOXYGEN_EXECUTABLE} "Doxyfile"
    WORKING_DIRECTORY
      "${PROJECT_BINARY_DIR}/doc"
  )

else()
  message (WARNING "No se ha encontrado Doxygen en el sistema, no se brinda soporte para la documentación.")
endif()
