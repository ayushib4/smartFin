import 'package:flutter/material.dart';
import 'package:smart_fin_flutter/widgets/traingle.dart';

class SentMessage extends StatelessWidget {
  const SentMessage({
    super.key,
    required this.message,
  });

  final String message;

  @override
  Widget build(BuildContext context) {
    final messageTextGroup = Flexible(
        child: Row(
      mainAxisAlignment: MainAxisAlignment.end,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Flexible(
          child: Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(
              color: Colors.grey[900],
              borderRadius: const BorderRadius.only(
                topLeft: Radius.circular(18),
                bottomLeft: Radius.circular(18),
                bottomRight: Radius.circular(18),
              ),
            ),
            child: Text(
              message,
              style: const TextStyle(
                  color: Colors.white, fontFamily: 'Monstserrat', fontSize: 14),
            ),
          ),
        ),
        CustomPaint(painter: Triangle(Colors.grey[900]!)),
      ],
    ));

    return Padding(
      padding: const EdgeInsets.only(right: 18.0, left: 50, top: 5, bottom: 5),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.end,
        children: <Widget>[
          const SizedBox(height: 30),
          messageTextGroup,
        ],
      ),
    );
  }
}
