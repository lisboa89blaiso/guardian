import json
from pathlib import Path


class MetadataService:

    def save(
        self,
        output_path,
        event_id,
        protocol,
        started_at,
        finished_at,
        duration_seconds,
        guardian_version="0.1.0"
    ):

        output_path = Path(output_path)

        metadata = {
            "event_id": event_id,
            "protocol": protocol,
            "started_at": started_at.isoformat(),
            "finished_at": finished_at.isoformat(),
            "duration_seconds": duration_seconds,
            "video_file": output_path.name,
            "guardian_version": guardian_version
        }

        json_path = output_path.with_suffix(".json")

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(
                metadata,
                f,
                indent=4,
                ensure_ascii=False
            )

        return json_path