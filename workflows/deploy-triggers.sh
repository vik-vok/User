BUILD_CONF='workflows/cloudbuild_template.yaml'
REPO_NAME="user"
REPO_OWNER="vik-vok"

# cloud-func-name | py_func_name | dir
array=(
  "${REPO_NAME}-get-all":"${REPO_NAME}_get_all":'functions/all'
  "${REPO_NAME}-delete":"${REPO_NAME}_delete":'functions/id/delete'
  "${REPO_NAME}-get":"${REPO_NAME}_get":'functions/id/get'
  "${REPO_NAME}-update":"${REPO_NAME}_update":'functions/id/update'
  "${REPO_NAME}-register":"${REPO_NAME}_register":'functions/register'
)

for i in "${array[@]}"; do
  IFS=":"
  set -- ${i}

  CLOUD_FUNC_NAME=${1}
  PY_FUNC_NAME="${2}"
  DIR="${3}"
  TRIGGER_NAME="${CLOUD_FUNC_NAME}-trigger"
  echo "#### Generating Trigger ${TRIGGER_NAME}"

#  gcloud alpha builds triggers delete "${TRIGGER_NAME}" --quiet
  gcloud beta builds triggers create github \
    --repo-name="${REPO_NAME}" \
    --repo-owner="${REPO_OWNER}" \
    --included-files="${DIR}/*" \
    --name="${TRIGGER_NAME}" \
    --branch-pattern="^master$" \
    --build-config=${BUILD_CONF} \
    --substitutions _CLOUD_FUNC_NAME="${CLOUD_FUNC_NAME}",_PY_FUNC_NAME="${PY_FUNC_NAME}",_DIR="${DIR}"
done