#include "io.hpp"
#include "lexer.hpp"
#include "arguments.hpp"

int main(int argc, char* argv[])
{
    Arguments args = parseArguments(argc,argv);
    if(args.help) show_help(std::string(argv[0]));
    else if(args.version) ; // show_version(version);
    else if(args.interactive) ; // repl();
    else if(!args.filename.empty())
    {
        std::string source = readFile(args.filename);   // Read the source code
        Tokens tokens = lex(&source);                   // Tokenize the source code

        for(Token token : tokens)
            std::cout << "(" << token.first << ") - " << token.second << std::endl;
    }

    return 0;
}