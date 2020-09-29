# Generated code sample for google.cloud.aiplatform.PipelineServiceClient.create_training_pipeline
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from uuid import uuid4
import pytest

from samples import (
    create_batch_prediction_job_video_object_tracking_sample,
    cancel_batch_prediction_job_sample,
    delete_batch_prediction_job_sample,
)

PROJECT_ID = "ucaip-sample-tests"
LOCATION = "us-central1"
MODEL_ID = "20547673299877888"  # Permanent horses model
DISPLAY_NAME = f"temp_create_batch_prediction_vot_test_{uuid4()}"
GCS_SOURCE_URI = (
    "gs://ucaip-samples-test-output/inputs/vot_batch_prediction_input.jsonl"
)
GCS_OUTPUT_URI = "gs://ucaip-samples-test-output/"

BATCH_PREDICTION_NAME = None


@pytest.fixture(scope="function", autouse=True)
def teardown(capsys):
    yield

    assert BATCH_PREDICTION_NAME is not None

    batch_prediction_job = BATCH_PREDICTION_NAME.split("/")[-1]

    # Stop the batch prediction job
    cancel_batch_prediction_job_sample.cancel_batch_prediction_job_sample(
        project=PROJECT_ID, batch_prediction_job_id=batch_prediction_job
    )

    # Delete the batch prediction job
    delete_batch_prediction_job_sample.delete_batch_prediction_job_sample(
        project=PROJECT_ID, batch_prediction_job_id=batch_prediction_job
    )

    out, _ = capsys.readouterr()
    assert "delete_batch_prediction_job_response" in out


# Creating AutoML Video Object Tracking batch prediction job
def test_ucaip_generated_create_batch_prediction_vcn_sample(capsys):
    global BATCH_PREDICTION_NAME
    assert BATCH_PREDICTION_NAME is None

    model_name = f'projects/{PROJECT_ID}/locations/{LOCATION}/models/{MODEL_ID}'

    create_batch_prediction_job_video_object_tracking_sample.create_batch_prediction_job_video_object_tracking_sample(
        project=PROJECT_ID,
        display_name=DISPLAY_NAME,
        model_name=model_name,
        gcs_source_uri=GCS_SOURCE_URI,
        gcs_destination_output_uri_prefix=GCS_OUTPUT_URI,
    )

    out, _ = capsys.readouterr()

    # Save resource name of the newly created batch prediction job
    BATCH_PREDICTION_NAME = out.split("name:")[1].split("\n")[0]