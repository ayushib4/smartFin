import 'package:flutter/material.dart';
import 'package:smart_fin_flutter/widgets/received_message.dart';
import 'package:video_player/video_player.dart';

class Agent extends StatefulWidget {
  const Agent({super.key, required this.mood, required this.response});

  final String mood;
  final String response;

  @override
  State<Agent> createState() => _AgentState();
}

class _AgentState extends State<Agent> {
  List messages = [];
  late VideoPlayerController _controller;
  late Future<void> _initializeVideoPlayerFuture;
  bool visibility = true;
  String response = "";

  @override
  void initState() {
    super.initState();

    response = widget.response;

    String mood = widget.mood;

    _controller = VideoPlayerController.asset(
      'assets/videos/$mood.mov',
    )..setLooping(true);
    _controller.setVolume(0.0);

    _initializeVideoPlayerFuture = _controller.initialize().then(
          (value) => _controller.play(),
        );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void hideReactions() {
    setState(() {
      visibility = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Padding(
              padding: const EdgeInsets.fromLTRB(16.0, 0.0, 16.0, 0.0),
              child: ReceivedMessage(message: response),
            ),
            FutureBuilder(
              future: _initializeVideoPlayerFuture,
              builder: (context, snapshot) {
                if (snapshot.connectionState == ConnectionState.done) {
                  return AspectRatio(
                    aspectRatio: _controller.value.aspectRatio,
                    child: VideoPlayer(_controller),
                  );
                } else {
                  return const Center(
                    child: CircularProgressIndicator(),
                  );
                }
              },
            ),
            Visibility(
              visible: visibility,
              child: Padding(
                padding: const EdgeInsets.fromLTRB(32.0, 8.0, 16.0, 0.0),
                child: Row(
                  children: [
                    OutlinedButton(
                      onPressed: () => hideReactions(),
                      child: const Icon(
                        Icons.thumb_up,
                        size: 20.0,
                        color: Colors.blue,
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.fromLTRB(8.0, 0.0, 0.0, 0.0),
                      child: OutlinedButton(
                        onPressed: () => hideReactions(),
                        child: const Icon(
                          Icons.thumb_down,
                          size: 20.0,
                          color: Colors.blue,
                        ),
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.fromLTRB(8.0, 0.0, 0.0, 0.0),
                      child: OutlinedButton(
                        onPressed: () => hideReactions(),
                        child: const Icon(
                          Icons.tag_faces_rounded,
                          size: 20.0,
                          color: Colors.blue,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
            const Padding(
              padding: EdgeInsets.fromLTRB(16.0, 16.0, 16.0, 16.0),
              child: TextField(
                decoration: InputDecoration(
                  border: OutlineInputBorder(),
                  labelText: 'Ask Mr. Wonderful a question',
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
